"""Validate intermediate checkpoints and retained regression functions."""

import argparse
import ast
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import xml.etree.ElementTree as ET


def git(repository: Path, *arguments: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repository), *arguments])


def test_functions(source: str) -> dict[str, str]:
    return {
        node.name: ast.dump(node, include_attributes=False)
        for node in ast.parse(source).body
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
    }


def verify_regressions(repository: Path, reference: str) -> None:
    paths = git(repository, "ls-tree", "-r", "--name-only", reference, "tests").decode().splitlines()
    count = 0
    for path in paths:
        if not path.endswith(".py"):
            continue
        before = test_functions(git(repository, "show", f"{reference}:{path}").decode())
        after = test_functions((repository / path).read_text())
        for name, definition in before.items():
            if after.get(name) != definition:
                raise SystemExit(f"Regression changed or removed: {path}::{name}")
            count += 1
    print(f"Retained {count} unchanged regression test functions from {reference}.", flush=True)


def verify_checkpoint(repository: Path, manifest_path: Path) -> None:
    manifest = json.loads(manifest_path.read_text())
    with tempfile.TemporaryDirectory(prefix="oop-checkpoint-") as temporary:
        workspace = Path(temporary)
        archive = git(repository, "archive", manifest["base_commit"])
        with tarfile.open(fileobj=io.BytesIO(archive)) as source:
            source.extractall(workspace, filter="data")
        for filename, target in manifest["files"].items():
            destination = workspace / target
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(manifest_path.parent / filename, destination)
        report = workspace / "checkpoint-results.xml"
        subprocess.run(
            [sys.executable, "-m", "pytest", "-q", f"--junitxml={report}"],
            cwd=workspace,
            check=True,
        )
        count = sum(int(suite.get("tests", "0")) for suite in ET.parse(report).getroot().findall("testsuite"))
        if count != manifest["expected_tests"]:
            raise SystemExit(f"{manifest_path.parent.name}: expected {manifest['expected_tests']} tests, found {count}")
        for conversation in manifest.get("sessions", []):
            result = subprocess.run(
                [sys.executable, "-m", "calculator"],
                cwd=workspace,
                input=conversation["input"],
                text=True,
                capture_output=True,
                timeout=15,
            )
            if result.returncode != conversation.get("exit_code", 0):
                raise SystemExit(f"Unexpected checkpoint session failure: {result.stderr}")
            for fragment in conversation.get("contains", []):
                if fragment not in result.stdout:
                    raise SystemExit(f"Missing checkpoint output: {fragment}")
            if conversation.get("stderr_contains", "") not in result.stderr:
                raise SystemExit("Checkpoint's expected failure did not occur")
        print(f"Checkpoint {manifest_path.parent.name}: {count} cases verified.", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--preserve-from")
    args = parser.parse_args()
    repository = args.repository.resolve()
    if args.preserve_from:
        verify_regressions(repository, args.preserve_from)
    manifests = sorted((repository / "checkpoints").glob("*/checkpoint.json"))
    for manifest in manifests:
        verify_checkpoint(repository, manifest)
    print(f"Verified {len(manifests)} intermediate checkpoints.")


if __name__ == "__main__":
    main()
