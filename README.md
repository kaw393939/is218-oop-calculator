# Stage 04: Connect history and removal to the REPL

[Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/03-basic-cli) · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/05-testing)

This branch is a worked checkpoint. Read it beside the separate project you are typing. [Full lessons and glossary](https://github.com/kaw393939/is218-oop-calculator/tree/main/docs) remain available on main.

[See exactly what changed](https://github.com/kaw393939/is218-oop-calculator/compare/stage/03-basic-cli...stage/04-complete-cli).

## Type or update these files

- [calculator/cli.py](calculator/cli.py)
- [tests/test_cli.py](tests/test_cli.py)

Keep files from previous stages unless this stage replaces them. Read each comment and predict what the code will do before running it.

## Run the checkpoint

From this project's root, with dependencies installed in your active virtual environment:

```bash
python -m pytest
python -m calculator
```

**Expected:** 12 tests pass. Add two entries, remove number 1, and confirm the remaining entry is renumbered to 1. Try removing 99 and entering hello as a number.

**Not included yet:** Comprehensive error-path tests, the coverage gate, and GitHub Actions.

**Explain before advancing:** Where do user numbers become Python indexes, and why is history only updated after validation?
