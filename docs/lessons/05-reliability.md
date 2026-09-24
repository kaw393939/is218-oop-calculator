# Stage 5: turn mistakes into tested behavior

[Previous lesson](04-repl.md) · [Worked branch](https://github.com/kaw393939/is218-oop-calculator/tree/learn/05-reliability) · [Next lesson](06-ci.md)

## Why this matters

A person entering `hello` should not lose the session. A removal mistake should not erase a different entry. Error handling is part of the behavior we promise, so it needs assertions just like successful arithmetic.

## What you already have

An interactive happy-path calculator with 19 tests and a recorded invalid-input failure. The model already rejects invalid history requests; the CLI still needs to translate those exceptions into helpful messages.

## What you will add

You will recover from expected errors, preserve history after rejected requests, read missing-line and branch reports, and finish with a meaningful coverage gate.

Update `calculator/cli.py`, expand the three files under `tests/`, and add `pytest.ini` **last**. [Compare with Stage 4](https://github.com/kaw393939/is218-oop-calculator/compare/learn/04-repl...learn/05-reliability).

## Type and run

### 1. Observe the gap

Before changing the code, run:

```bash
python -m pytest --cov=calculator --cov-branch --cov-report=term-missing
```

The tests can pass while the report shows missing paths. Coverage tells you where tests have not executed code; it does not say which behavior is correct. Write down one uncovered path and the input you think would reach it.

### 2. Handle the recorded failure

Update `cli.py` in sections. Start with `read_number` and the operation's `try`/`except ValueError`. Invalid input prints feedback and uses `continue` to return to the command prompt. Save a calculation only after validation succeeds. The worked version rejects NaN, infinity, and overflowed results too.

Next handle invalid removal text separately from an out-of-range index. Finally add the outer EOF/KeyboardInterrupt handler. That outer block covers all input prompts, including operands and removal numbers.

Run the existing tests after each section. Manually try an invalid operand, then a successful addition in the same session. Confirm history includes only the successful calculation.

### 3. Assert what the application promises

Read and type the expanded tests one behavior at a time:

| Behavior | What the test must establish |
| --- | --- |
| Invalid arithmetic input | A useful message, no saved calculation, and a later successful command. |
| Invalid removal | A useful message and unchanged existing history. |
| Empty history | Clear feedback without requesting an impossible removal. |
| First, middle, and last removal | The correct object is returned and remaining order is preserved. |
| Interrupted input | A clean farewell from every prompt position. |

The final tests use parametrization to repeat one assertion pattern with different inputs. Read a table row as arguments to the function below it. Stacked decorators generate combinations. `pytest.approx` accommodates floating-point rounding. A list comprehension is a compact loop that builds a list. In `["add", *operands, "exit"]`, `*operands` inserts each operand into the script. `pytest.raises` checks an expected exception.

The entry-point and interruption tests are supporting techniques; focus first on the behavior each asserts. Run coverage again, inspect remaining paths, and add the relevant assertions before enforcing the final threshold.

### 4. Make the expectation repeatable

Type `pytest.ini` only after the suite is complete. It enables coverage for the application, measures branches, prints missing paths, and fails below 100%.

```bash
python -m pytest
```

**Expect:** 49 cases pass and line/branch coverage reaches 100%, without custom application exclusions. If you add meaningful cases, your count may be higher. For an unfinished experiment after the gate is installed, use `--cov-fail-under=0` temporarily on the command line; restore the default command for completion.

For a visual report, run `python -m pytest --cov-report=term-missing --cov-report=html` and open `htmlcov/index.html`. Generated reports stay out of Git.

## Explain and experiment

Choose a case you could not reach with the original tests. Explain the input, the relevant branch, and the assertion that would detect incorrect behavior. Temporarily change its expected message or result, observe a failure, then restore it.

## Check your understanding

1. Why validate before saving the object?
2. Why is catching every exception indiscriminately a poor substitute for understanding expected failures?
3. Can 100% coverage prove that the arithmetic is right?

<details>
<summary>Self-check after you explain</summary>

Rejected work should not enter history. Specific handlers distinguish expected user mistakes while allowing unrelated programming defects to surface. Coverage demonstrates execution; assertions and review establish whether the results and state changes satisfy the contract.

</details>

**Ready to move on:** demonstrate recovery after a mistake, explain a missing-path test, and pass the default coverage-enforced command. Commit with `git add calculator tests pytest.ini` and `git commit -m "Stage 5: test error paths and enforce coverage"`.
