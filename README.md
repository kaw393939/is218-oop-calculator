# Stage 01: Create calculation objects

[Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/00-setup) · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/02-history)

This branch is a worked checkpoint. Read it beside the separate project you are typing. [Full lessons and glossary](https://github.com/kaw393939/is218-oop-calculator/tree/main/docs) remain available on main.

[See exactly what changed](https://github.com/kaw393939/is218-oop-calculator/compare/stage/00-setup...stage/01-calculations).

## Type or update these files

- [calculator/__init__.py](calculator/__init__.py)
- [calculator/calculation.py](calculator/calculation.py)
- [tests/test_calculation.py](tests/test_calculation.py)

Keep files from previous stages unless this stage replaces them. Read each comment and predict what the code will do before running it.

## Run the checkpoint

From this project's root, with dependencies installed in your active virtual environment:

```bash
python -m pytest
```

**Expected:** 4 tests pass. Change the first expected result to 16, inspect the failure, then restore 15.

**Not included yet:** History, interactive input, and a coverage threshold.

**Explain before advancing:** How can the same get_result() call produce different behavior?
