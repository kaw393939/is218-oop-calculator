# Stage 5: fix one failure at a time

[Previous lesson](https://github.com/kaw393939/is218-oop-calculator/blob/learn/04-repl/docs/lessons/04-repl.md) · [Worked branch](https://github.com/kaw393939/is218-oop-calculator/tree/learn/05-reliability) · [Next lesson](https://github.com/kaw393939/is218-oop-calculator/blob/learn/06-ci/docs/lessons/06-ci.md)

## Why this matters

A typing mistake should not end a session or corrupt valid work. We will keep every earlier regression test and add focused assertions as we handle failures. Learning new test syntax is not a prerequisite for making the program reliable.

## What you already have

Stage 4's calculator, **19 reference tests**, and the `hello` crash. Preserve all previous tests, including the independent-instance check and your own additions.

## What you will add

**5A: invalid operands → 5B: invalid removal → 5C: remaining boundaries and coverage gate.** Parametrization is an optional cleanup after the behavior is correct.

[Compare with Stage 4](https://github.com/kaw393939/is218-oop-calculator/compare/learn/04-repl...learn/05-reliability). The final root test files retain the earlier test functions and append new ones. Intermediate references below show smaller increments.

## Type and run

### First, see what coverage cannot tell you

In your unchanged Stage 4 solution, run:

```bash
python -m pytest --cov=calculator --cov-branch --cov-report=term-missing
```

The unextended reference reports **100% for `cli.py` and 98% overall**; only the entry-point module is unexecuted. Your additions may change the total.

Now run `python -m calculator` and enter `add`, then `hello`. It still crashes. The existing CLI paths were executed, but input recovery was never implemented. Coverage cannot report a missing branch that does not exist. **Requirements identify missing behavior; assertions check it; coverage identifies unexecuted code.** Keep this observation in your notes.

### 5A — Invalid operands

Use [Checkpoint 5A](https://github.com/kaw393939/is218-oop-calculator/tree/learn/05-reliability/checkpoints/05a). Before changing the CLI, append `test_invalid_first_number_recovers` from its test reference and run it:

```bash
python -m pytest tests/test_cli.py -k invalid_first_number
```

**Expect a failure** caused by converting `hello` to a float. Update the operation block in `cli.py` to catch `ValueError` before saving the object. Invalid input prints feedback and `continue` returns to the next command.

Rerun that one test; it should pass. Append the invalid-second-number test, then run the entire suite. **21 reference cases pass**, and the earlier 19 remain present.

Manually enter invalid input, then a valid addition in the same session. Only the successful calculation should enter history. Save or commit this checkpoint before proceeding.

### 5B — Invalid removal

Use [Checkpoint 5B](https://github.com/kaw393939/is218-oop-calculator/tree/learn/05-reliability/checkpoints/05b). Append the two removal tests first. Run them with `python -m pytest tests/test_cli.py -k invalid_removal` and observe the current failures.

Add the removal handlers. `ValueError` means the text is not an integer; `IndexError` means there is no such entry. A `try` statement's `else` runs only when its protected block succeeded, so it can print the removed object.

Run the same tests, then the full suite: **23 reference cases pass**. The tests assert both the error message and preserved entries. Their ordinary loops try several boundary values; assertion messages identify which value failed.

### 5C — Complete the behavior, then enforce coverage

Use the root [CLI](https://github.com/kaw393939/is218-oop-calculator/blob/learn/05-reliability/calculator/cli.py) and [tests](https://github.com/kaw393939/is218-oop-calculator/tree/learn/05-reliability/tests). Keep the tests already written and append the remaining cases. Add each handler with its associated assertions, running after each group:

| Work | Evidence to check |
| --- | --- |
| Reject nonfinite operands and overflow | NaN, infinity, and an overflowed result never enter history. |
| Handle interrupted input | EOF and Ctrl+C end cleanly at the command, operand, and removal prompts. |
| Check collection boundaries | Empty, middle, last, and only-entry removal preserve the intended state. |
| Check the package entry point | `python -m calculator`'s entry module starts the REPL. |
| Check arithmetic boundaries | Decimal and negative operands produce the expected results. |

`isfinite` distinguishes ordinary finite numbers from NaN and infinity. The outer exception handler covers every prompt. The interruption test supplies answers up to a chosen prompt, then raises the expected interruption; its loops cover multiple scenarios without decorators. `runpy` exercises the entry module within the test process. `pytest.approx` allows tiny floating-point rounding differences for decimal addition.

Run coverage again **before** typing the final configuration. Inspect missing lines, state the behavior that would execute them, and add an assertion about the expected outcome. Do not delete code or exclude lines to improve the percentage.

Only after all checks pass, type the root `pytest.ini` and run:

```bash
python -m pytest
```

**Expect:** 37 named reference tests and **100% line and branch coverage**. Some tests loop over multiple input examples. Your independent tests may increase the total. All original 19 test functions are retained.

For a visual report, run `python -m pytest --cov-report=term-missing --cov-report=html` and open `htmlcov/index.html`. If investigating an incomplete experiment after installing the gate, use `--cov-fail-under=0` temporarily; restore the default command for completion.

## Explain and experiment

Explain one case where requirements revealed missing behavior, then one case where coverage revealed an unexecuted path. What assertion makes each test meaningful?

### Build something independently

Write one conversation test that makes two unsuccessful removal attempts, then successfully removes the original item and confirms history is empty. Choose your own inputs and assert that the failed attempts did not corrupt the state. Keep it.

### Optional cleanup: learn parametrization afterward

[Parametrization as a refactoring](https://github.com/kaw393939/is218-oop-calculator/blob/main/docs/optional-parametrization.md) translates a familiar loop into a data-driven test. It is optional, introduces no new application requirement, and should preserve the same behavior assertions. The required worked suite uses ordinary functions and loops.

## Check your understanding

1. Why can the Stage 4 CLI have 100% coverage and still crash on `hello`?
2. Why should a rejected request leave existing history unchanged?
3. Why keep older tests when adding more detailed ones?

<details>
<summary>Self-check after you explain</summary>

Coverage measures execution of existing code, not completeness of requirements. Rejecting a request should not undo previous successful work. Older tests protect earlier promises, including independent instance state, while new tests broaden the behavior checked.

</details>

**Ready to move on:** demonstrate recovery, explain the coverage counterexample, and pass the default coverage-enforced suite. Commit your code, tests, and pytest configuration.
