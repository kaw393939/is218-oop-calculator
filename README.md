# Stage 03: Build a small interactive calculator

[Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/02-history) · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/04-complete-cli)

This branch is a worked checkpoint. Read it beside the separate project you are typing. [Full lessons and glossary](https://github.com/kaw393939/is218-oop-calculator/tree/main/docs) remain available on main.

[See exactly what changed](https://github.com/kaw393939/is218-oop-calculator/compare/stage/02-history...stage/03-basic-cli).

## Type or update these files

- [calculator/cli.py](calculator/cli.py)
- [calculator/__main__.py](calculator/__main__.py)
- [tests/test_cli.py](tests/test_cli.py)

Keep files from previous stages unless this stage replaces them. Read each comment and predict what the code will do before running it.

## Run the checkpoint

From this project's root, with dependencies installed in your active virtual environment:

```bash
python -m pytest
python -m calculator
```

**Expected:** 11 tests pass. Try add → 10 → 5, subtract → 20 → 7, help, pizza, and exit.

**Not included yet:** The history and remove commands. History exists but the CLI does not use it yet.

**Explain before advancing:** What does continue do after invalid input, and how does it differ from break?
