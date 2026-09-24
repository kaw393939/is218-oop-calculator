# Stage 5: Recover from errors and investigate coverage

[Course home](https://github.com/kaw393939/is218-oop-calculator) · [Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/04-repl) · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/06-ci)

Make invalid requests safe one checkpoint at a time, retaining all 19 earlier regression functions.

**Start with [the lesson](docs/lessons/05-reliability.md)**. It explains the file order, small checkpoints, experiments, and self-check questions. Use this branch as a worked reference beside the separate solution you are typing.

## Smaller checkpoints

Start with [5A: invalid operands](checkpoints/05a/README.md) for 21 tests, then [5B: invalid removal](checkpoints/05b/README.md) for 23. The root files complete 5C with 37 tests and full coverage. Preserve earlier tests and your independent additions.

Reference counts exclude your independent tasks; a higher passing count is expected when you keep those tests.

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

Expect **37 passing test cases** in this worked snapshot. The default test command enforces 100% line and branch coverage. Some tests cover multiple scenarios with loops; all 19 Stage 4 test functions remain unchanged.

## Stage boundary

Use 5A for operand recovery, 5B for removal recovery, and 5C for remaining boundaries. Keep earlier tests and type pytest.ini last. Parametrization is optional cleanup; the required suite uses familiar functions and loops.

Explain this lesson's exit questions and restore any deliberate experiments before committing your solution and moving on. Shared course documents in this branch are a publication snapshot; the [current course home](https://github.com/kaw393939/is218-oop-calculator) carries later introductory updates.
