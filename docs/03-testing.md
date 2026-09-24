# 3. Test behaviors and investigate coverage

[Previous: build](02-build.md) · [Next: GitHub Actions](04-github-actions.md)

Tests should check what a program does, not simply execute its methods. Read each test, predict its assertion, then type it into the matching file in your project.

## Build the suite in stages

First type [pytest.ini](../pytest.ini). It locates the tests and application package, enables line and branch coverage, prints missing paths, and enforces a final 100% threshold.

While the suite is incomplete, temporarily override the threshold **in the command**, not in the configuration:

| Type this file | Run this checkpoint |
| --- | --- |
| [tests/test_calculation.py](../tests/test_calculation.py) | `python -m pytest tests/test_calculation.py --cov-fail-under=0` |
| [tests/test_history.py](../tests/test_history.py) | `python -m pytest tests/test_history.py --cov-fail-under=0` |
| [tests/test_cli.py](../tests/test_cli.py) | `python -m pytest --cov-fail-under=0` |

The calculation tests cover arithmetic, abstraction, and polymorphism. History tests verify ordering, removal boundaries, and collection ownership. CLI tests simulate input and assert printed output, including recovery after errors and interrupted input.

`monkeypatch` temporarily replaces `input()` with scripted responses; `capsys` captures output. Both are pytest fixtures. Parametrized tests run the same behavior check with several inputs.

## Use coverage as feedback

1. Run a checkpoint and look at the `Missing` column.
2. Read the indicated application code. Which behavior would execute it?
3. Add a test with assertions about the expected output or state.
4. If that test reveals a bug, fix the application and rerun.

For example, an uncovered invalid-removal branch suggests a test using an out-of-range index. Assert both that it raises `IndexError` and that history stays unchanged. At the CLI level, check that the message appears and the next command works.

For a visual report:

```bash
python -m pytest --cov-fail-under=0 --cov-report=term-missing --cov-report=html
```

Open `htmlcov/index.html`. Reports are generated locally and should not be committed.

**Exercise:** before typing the invalid-removal tests, inspect their missing paths in the report. Add those tests, rerun, and describe what changed. Do not delete application behavior or exclude lines just to improve coverage.

## Final checkpoint

```bash
python -m pytest
```

The reference project has **49 passing test cases and 100% line and branch coverage**. The default command must pass without lowering the threshold.

Coverage measures execution, not correctness. A wrong result can still have 100% coverage if assertions are missing or incorrect. Explain what each test proves before considering it complete.
