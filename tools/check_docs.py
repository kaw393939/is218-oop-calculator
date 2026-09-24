"""Check each branch's teaching scope, Markdown links, and lesson structure."""

import argparse
import ast
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_URL = "https://github.com/kaw393939/is218-oop-calculator"
ARCHIVE_TAG = "archive/legacy-course-v1"
# A worked branch carries only its own lesson and intermediate checkpoints.
STAGES = {
    "main": (),
    "learn/01-objects": (),
    "learn/02-abstraction": ("02a",),
    "learn/03-history": (),
    "learn/04-repl": ("04a", "04b"),
    "learn/05-reliability": ("05a", "05b"),
    "learn/06-ci": (),
}
LESSON_SECTIONS = (
    "Why this matters",
    "What you already have",
    "What you will add",
    "Type and run",
    "Explain and experiment",
    "Check your understanding",
)


def repository_link_error(root: Path, stage: str, target: str) -> str | None:
    """Check private repository links from the checkout, without HTTP access."""
    if not target.startswith(REPOSITORY_URL + "/"):
        return None
    route = unquote(urlsplit(target).path).split("/", 3)[-1]
    kind, _, location = route.partition("/")
    if kind not in ("blob", "tree", "compare"):
        return None

    def object_type(reference: str, path: str | None = None) -> str:
        if reference == stage:
            if path is None:
                return "commit"
            destination = root / path
            return "tree" if destination.is_dir() else "blob" if destination.is_file() else ""
        revision = f"refs/tags/{reference}" if reference == ARCHIVE_TAG else f"origin/{reference}"
        revision += f":{path}" if path is not None else "^{commit}"
        result = subprocess.run(
            ["git", "-C", str(root), "cat-file", "-t", revision],
            capture_output=True, text=True,
        )
        return result.stdout.strip() if result.returncode == 0 else ""

    if kind == "compare":
        references = location.split("...")
        if len(references) != 2 or any(
            ref not in (*STAGES, ARCHIVE_TAG) or object_type(ref) != "commit" for ref in references
        ):
            return f"missing or unsupported comparison ref: {target}"
        return None
    for reference in (*STAGES, ARCHIVE_TAG):
        if location == reference or location.startswith(reference + "/"):
            path = location[len(reference):].lstrip("/")
            if object_type(reference, path) != kind:
                return f"missing {kind} target: {target}"
            return None
    return f"unknown teaching branch: {target}"


def main(root: Path, stage: str) -> None:
    files = [root / "README.md", *sorted((root / "docs").rglob("*.md"))]
    files += sorted((root / "checkpoints").glob("*/README.md"))
    errors = []
    for path in files:
        source = path.read_text()
        # Code examples can contain []() syntax that is not a Markdown link.
        prose = re.sub(r"```.*?```", "", source, flags=re.DOTALL)
        prose = re.sub(r"`[^`]*`", "", prose)
        for target in re.findall(r"\]\(([^)]+)\)", prose):
            error = repository_link_error(root, stage, target)
            if error:
                errors.append(f"{path.relative_to(root)}: {error}")
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            relative_path = target.split("#", 1)[0]
            if not (path.parent / relative_path).exists():
                errors.append(f"{path.relative_to(root)}: missing {target}")
        for snippet in re.findall(r"```python\n(.*?)```", source, re.DOTALL):
            try:
                ast.parse(snippet)
            except SyntaxError as error:
                errors.append(f"{path.relative_to(root)}: invalid Python example: {error}")
        if path.parent.name == "lessons":
            for heading in LESSON_SECTIONS:
                if f"## {heading}\n" not in source:
                    errors.append(f"{path.name}: missing lesson section {heading}")
            for label, target in re.findall(r"\[(Previous lesson|Next lesson)\]\(([^)]+)\)", source):
                destination = Path(target).stem
                expected = (
                    "https://github.com/kaw393939/is218-oop-calculator/blob/learn/"
                    f"{destination}/docs/lessons/{destination}.md"
                )
                if target != expected:
                    errors.append(f"{path.name}: {label} must select the matching branch")
            if "### Build something independently" not in source:
                errors.append(f"{path.name}: missing independent task")
    lesson_root = root / "docs" / "lessons"
    lessons = {path.relative_to(lesson_root).as_posix() for path in lesson_root.rglob("*.md")}
    expected_lessons = set() if stage == "main" else {stage.split("/")[1] + ".md"}
    if lessons != expected_lessons:
        errors.append(f"{stage}: expected lessons {sorted(expected_lessons)}, found {sorted(lessons)}")
    if stage != "main":
        documents = {
            path.relative_to(root / "docs").as_posix()
            for path in (root / "docs").rglob("*") if path.is_file()
        }
        expected_documents = {f"lessons/{name}" for name in expected_lessons}
        if documents != expected_documents:
            errors.append(f"{stage}: docs must contain only its own lesson; found {sorted(documents)}")
    checkpoints = {path.name for path in (root / "checkpoints").glob("*") if path.is_dir()}
    if checkpoints != set(STAGES[stage]):
        errors.append(f"{stage}: expected checkpoints {list(STAGES[stage])}, found {sorted(checkpoints)}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(files)} documents, {len(lessons)} lessons, and {len(checkpoints)} checkpoints for {stage}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--stage", choices=STAGES, default="main")
    args = parser.parse_args()
    main(args.root.resolve(), args.stage)
