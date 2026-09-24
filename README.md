# Stage 02: Let History manage a collection

[Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/01-calculations) · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/03-basic-cli)

This branch is a worked checkpoint. Read it beside the separate project you are typing. [Full lessons and glossary](https://github.com/kaw393939/is218-oop-calculator/tree/main/docs) remain available on main.

[See exactly what changed](https://github.com/kaw393939/is218-oop-calculator/compare/stage/01-calculations...stage/02-history).

## Type or update these files

- [calculator/history.py](calculator/history.py)
- [tests/test_history.py](tests/test_history.py)

Keep files from previous stages unless this stage replaces them. Read each comment and predict what the code will do before running it.

## Run the checkpoint

From this project's root, with dependencies installed in your active virtual environment:

```bash
python -m pytest
```

**Expected:** 9 tests pass. The collection accepts both operation types and protects its internal list.

**Not included yet:** The terminal interface and comprehensive boundary tests.

**Explain before advancing:** Why does History contain calculations rather than inherit from Calculation?
