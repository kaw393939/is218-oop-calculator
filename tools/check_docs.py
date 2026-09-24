"""Maintainer check: validate local Markdown targets and lesson structure."""

import ast
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
LESSON_SECTIONS = (
    "Why this matters",
    "What you already have",
    "What you will add",
    "Type and run",
    "Explain and experiment",
    "Check your understanding",
)


def main() -> None:
    files = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]
    errors = []
    for path in files:
        source = path.read_text()
        # Code examples can contain []() syntax that is not a Markdown link.
        prose = re.sub(r"```.*?```", "", source, flags=re.DOTALL)
        prose = re.sub(r"`[^`]*`", "", prose)
        for target in re.findall(r"\]\(([^)]+)\)", prose):
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            relative_path = target.split("#", 1)[0]
            if not (path.parent / relative_path).exists():
                errors.append(f"{path.relative_to(ROOT)}: missing {target}")
        for snippet in re.findall(r"```python\n(.*?)```", source, re.DOTALL):
            try:
                ast.parse(snippet)
            except SyntaxError as error:
                errors.append(f"{path.relative_to(ROOT)}: invalid Python example: {error}")
        if path.parent.name == "lessons":
            for heading in LESSON_SECTIONS:
                if f"## {heading}\n" not in source:
                    errors.append(f"{path.name}: missing lesson section {heading}")
    lessons = list((ROOT / "docs" / "lessons").glob("*.md"))
    if len(lessons) != 6:
        errors.append(f"Expected six lessons, found {len(lessons)}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(files)} documents, six lesson structures, and Python example syntax.")


if __name__ == "__main__":
    main()
