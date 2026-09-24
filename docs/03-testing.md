# 3. Test behaviors and investigate coverage

[Previous: build](02-build.md) · [Next: GitHub Actions](04-github-actions.md)

Tests should check what a program does, not simply execute its methods. Read each test, predict its assertion, then type it into the matching file in your project.

## Your first test

Do this as soon as you finish `calculation.py`. Create `tests/test_first.py` with:

```python
from calculator.calculation import Add


def test_add():
    calculation = Add(10, 5)            # Arrange: prepare an example.
    result = calculation.get_result()  # Act: ask the object to work.
    assert result == 15                # Assert: check the answer.
```

Run `python -m pytest tests/test_first.py`. Before `pytest.ini` exists, this just runs the test. If you already created that configuration, append `--cov-fail-under=0` while building the suite.

Change the expected answer to `16` and run again. Read the failure: the test expected `16` but received `15`. Restore `15` and rerun. This shows what an assertion contributes beyond executing code.

Delete this temporary practice file when you type `test_calculation.py`; its parametrized table includes the same case. In that table, `(Add, 10, 5, 15)` supplies the four arguments to `test_arithmetic`. The decorator turns one test function into multiple cases.

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

Think of a CLI test as rehearsing a conversation: `['add', '10', '5', 'exit']` is what the user says; the captured output is what the app says back. `iter(answers)` creates a cursor over that script, `next(responses)` takes one answer, and `lambda prompt: ...` is a small unnamed function used in place of `input`. Pytest restores the original function afterward. `*operands` in a list inserts each operand into the scripted conversation.

Start by understanding `session()` and `test_assignment_session()`. Then read error tests. The `runpy` entry-point test and interruption simulation are advanced supporting checks; you do not need to master those tools to explain inheritance or polymorphism.

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
