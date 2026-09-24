# Stage 4: build the conversation in three small steps

[Previous lesson](https://github.com/kaw393939/is218-oop-calculator/blob/learn/03-history/docs/lessons/03-history.md) · [Worked branch](https://github.com/kaw393939/is218-oop-calculator/tree/learn/04-repl) · [Next lesson](https://github.com/kaw393939/is218-oop-calculator/blob/learn/05-reliability/docs/lessons/05-reliability.md)

## Why this matters

A person should be able to use the model without writing Python expressions. We will build that conversation before introducing tools that automate it.

## What you already have

The calculation and history classes, with **15 reference tests**. Keep your own tests. This stage assumes valid finite operands and valid removal numbers; Stage 5 will handle mistakes.

## What you will add

**4A: arithmetic and exit → 4B: history and removal → 4C: automated conversations.** Each checkpoint runs independently in your solution before you advance.

[Compare with Stage 3](https://github.com/kaw393939/is218-oop-calculator/compare/learn/03-history...learn/04-repl). The root files show the completed stage. Intermediate worked source is linked below; do not skip straight to the completed tests.

## Type and run

### 4A — A small working REPL

Open [Checkpoint 4A](https://github.com/kaw393939/is218-oop-calculator/tree/learn/04-repl/checkpoints/04a). Type `cli.py` into `calculator/cli.py` and `entrypoint.py` into `calculator/__main__.py`. Keep all other files.

From your solution root:

```bash
python -m pytest
python -m calculator
```

**Expect:** your 15 model tests still pass. Then try `add → 10 → 5`, `subtract → 20 → 7`, `help`, and `exit`. Expect results `15` and `13`, then a farewell. There are no history commands or CLI tests in this checkpoint yet.

Read the loop in four steps: **read** text, **evaluate** the request, **print** its result, then **loop**. `break` leaves the loop. `strip().lower()` normalizes commands. `float` converts operand text.

The dictionary stores classes. Selecting `operations[command]` chooses a class; calling it with `(a, b)` creates an instance. This is separate from storing an object in history.

**Pause:** explain one full request before adding commands.

### 4B — Connect History

Open [Checkpoint 4B](https://github.com/kaw393939/is218-oop-calculator/tree/learn/04-repl/checkpoints/04b). Update `calculator/cli.py`; the entry point is unchanged. Read the helper functions first, then the changes to `run`.

Run `python -m pytest` again: the same **15 reference tests** pass. Run the app and try:

| Type | Expect |
| --- | --- |
| `add`, `10`, `5` | `Result: 15` |
| `subtract`, `20`, `7` | `Result: 13` |
| `history` | Two numbered entries. |
| `remove`, `1` | Addition removed. |
| `history` | Subtraction is now entry 1. |
| `exit` | `Goodbye!` |

`describe` asks any calculation for its result. An f-string inserts values; `:g` formats numbers compactly. `enumerate(..., start=1)` numbers entries for people. `number - 1` translates that display number to a Python index.

**Pause:** point to the line that constructs the object and the separate line that saves it. Explain why History needs no new arithmetic logic.

### 4C — Automate the conversation you just tried

Now type the root [tests/test_cli.py](https://github.com/kaw393939/is218-oop-calculator/blob/learn/04-repl/tests/test_cli.py), first the imports, helper, and `test_arithmetic_session` only. Run `python -m pytest`: expect **16 reference cases**. Add the remaining three tests and rerun: expect **19**.

`monkeypatch` temporarily replaces `input` with a function supplying scripted answers. `capsys` captures printed output. `iter` creates a cursor; `next` consumes one answer per prompt. Pytest restores input afterward. Read the list as the user's side of a conversation and the assertions as checks on the app's replies.

## Explain and experiment

Change a prompt's wording and rerun just the arithmetic tests with `python -m pytest tests/test_calculation.py`. Restore it afterward. Why should arithmetic not depend on prompt wording?

Try `add` followed by `hello` in the app. It crashes at this checkpoint. Save the final traceback line; this intentionally unfinished behavior motivates Stage 5. Restart the app to continue.

### Build something independently

Write your own scripted-session test using a mixed-case arithmetic command surrounded by spaces, with operands not used in the worked conversation. Check the numerical reply and clean exit. Keep the test; no worked solution is provided.

## Check your understanding

1. How are construction, storage, and display different responsibilities?
2. Why does removal use `number - 1`?
3. What did the manual conversation tell you that the 15 model tests did not?

<details>
<summary>Self-check after you explain</summary>

The selected class constructs an operation, History manages its membership, and the CLI presents it. User numbering starts at 1; list indexing starts at 0. Model tests check the objects, while a terminal conversation also checks their connection to user input and output.

</details>

**Ready to move on:** reproduce the successful session, explain the invalid-input crash, and pass 19 reference tests plus your additions. Commit the stage before changing reliability behavior.
