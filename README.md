# Stage 5: Recover from errors and investigate coverage

[Course home](https://github.com/kaw393939/is218-oop-calculator) · [Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/04-repl) · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/06-ci)

Make invalid requests safe, assert preserved state, and use missing coverage to find behavior needing attention.

**Start with [the lesson](docs/lessons/05-reliability.md)**. It explains the file order, small checkpoints, experiments, and self-check questions. Use this branch as a worked reference beside the separate solution you are typing.

## Files added or changed

- [calculator/cli.py](calculator/cli.py)
- [tests/test_calculation.py](tests/test_calculation.py)
- [tests/test_history.py](tests/test_history.py)
- [tests/test_cli.py](tests/test_cli.py)
- [pytest.ini](pytest.ini)

[Inspect changes from the previous stage](https://github.com/kaw393939/is218-oop-calculator/compare/learn/04-repl...learn/05-reliability).

## Verify this checkpoint

With dependencies installed and your virtual environment active, run from this project's root:

```bash
python -m pytest
python -m calculator
```

Expect **49 passing test cases** in this worked snapshot. The default test command enforces 100% line and branch coverage.

## Stage boundary

The application and final test suite are complete. Type pytest.ini last during the lesson: investigate missing paths before enforcing the final 100% gate. GitHub Actions arrives in Stage 6.

Explain this lesson's exit questions and restore any deliberate experiments before committing your solution and moving on. Shared course documents in this branch are a publication snapshot; the [current course home](https://github.com/kaw393939/is218-oop-calculator) carries later introductory updates.
