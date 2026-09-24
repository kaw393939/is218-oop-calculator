# Stage 4: let a person use the objects

[Previous lesson](03-history.md) · [Worked branch](https://github.com/kaw393939/is218-oop-calculator/tree/learn/04-repl) · [Next lesson](05-reliability.md)

## Why this matters

So far, Python experiments and tests are the only callers. A command-line interface lets a person use the same objects without writing Python expressions. The interface translates input into requests; calculation objects still own arithmetic and History still manages the collection.

## What you already have

The complete model and 15 passing tests. This stage is a **happy-path checkpoint**: use valid finite numbers and existing removal entries. Numeric mistakes can still raise exceptions; Stage 5 will fix that deliberately exposed limitation.

## What you will add

You will build the REPL, separate display from arithmetic, convert displayed numbers to list indexes, and automate one terminal conversation.

Type in this order:

1. `calculator/cli.py`: imports, HELP, `describe`, and `show_history` first; then `run`.
2. `calculator/__main__.py`: the package entry point.
3. `tests/test_cli.py`: scripted conversations and output assertions.

[Compare with Stage 3](https://github.com/kaw393939/is218-oop-calculator/compare/learn/03-history...learn/04-repl).

## Type and run

After typing the helpers, use a fresh Python prompt:

```python
from calculator.cli import describe
from calculator.calculation import Add
print(describe(Add(10, 5)))
```

**Expect:** `Add: 10, 5 = 15`. The class name supplies a label; `get_result()` supplies behavior. An f-string inserts values; `:g` displays a float compactly.

Exit Python and finish `run`. Trace its pieces:

1. **Read:** `input` gives text; `strip().lower()` normalizes the command.
2. **Evaluate:** select an operation class, read operands, construct an object, and store it.
3. **Print:** display the result or history.
4. **Loop:** return to the prompt until `break` handles `exit`.

The dictionary stores classes, not instances. `operation_class = operations[command]` selects `Add` or `Subtract`; `operation_class(a, b)` creates the chosen kind of object. `float(input(...))` converts text into a number.

After typing `__main__.py`, run `python -m calculator` from the terminal and follow this conversation:

| Type | Expect |
| --- | --- |
| `add`, then `10`, then `5` | `Result: 15` |
| `subtract`, then `20`, then `7` | `Result: 13` |
| `history` | Two entries numbered 1 and 2. |
| `remove`, then `1` | Addition removed; subtraction remains. |
| `history` | Subtraction is now numbered 1. |
| `help`, then `exit` | Command help, then a farewell. |

Type the tests and run `python -m pytest`: expect 19 passing cases. `monkeypatch` temporarily replaces `input` with a function that supplies scripted answers. `capsys` captures printed text. `iter` makes a cursor over answers; `next` consumes one answer per prompt. Pytest restores the original input function afterward.

## Explain and experiment

Change one prompt's wording, rerun the arithmetic tests, and restore it. Why should arithmetic behavior not depend on that text?

Now try `add` followed by `hello`. Save the final traceback line in your notes. This failure is expected at this checkpoint and becomes the first problem in Stage 5. Restart the program to continue using it.

## Check your understanding

1. Where is the operation constructed, and where is it stored?
2. Why does removal use `number - 1`?
3. How do `return` and `break` differ?

<details>
<summary>Self-check after you explain</summary>

The selected class constructs the object; `history.add` records it. Display numbering starts at 1, while Python indexes start at 0. `return` leaves a function; `break` leaves the nearest loop. The farewell prints after the loop ends.

</details>

**Ready to move on:** reproduce the valid session, explain the known invalid-input failure, and pass 19 tests. Commit with `git add calculator tests` and `git commit -m "Stage 4: connect the model to a REPL"`.
