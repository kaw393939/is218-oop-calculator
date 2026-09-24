# Stage 05: Use coverage to complete the test suite

[Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/04-complete-cli) · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/06-final)

This branch is a worked checkpoint. Read it beside the separate project you are typing. [Full lessons and glossary](https://github.com/kaw393939/is218-oop-calculator/tree/main/docs) remain available on main.

[See exactly what changed](https://github.com/kaw393939/is218-oop-calculator/compare/stage/04-complete-cli...stage/05-testing).

## Type or update these files

- [tests/test_calculation.py](tests/test_calculation.py)
- [tests/test_history.py](tests/test_history.py)
- [tests/test_cli.py](tests/test_cli.py)
- [pytest.ini](pytest.ini)

Keep files from previous stages unless this stage replaces them. Read each comment and predict what the code will do before running it.

## Run the checkpoint

From this project's root, with dependencies installed in your active virtual environment:

```bash
python -m pytest
```

**Expected:** 49 tests pass with 100% line and branch coverage. Read each missing-path test and identify its assertion before typing it.

**Not included yet:** GitHub Actions. All application features and final tests are present.

**Explain before advancing:** Why can 100% coverage still accompany an incorrect program?
