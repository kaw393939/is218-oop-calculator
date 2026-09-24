# 2. Type and understand the calculator

[Previous: setup](01-setup.md) · [Next: testing](03-testing.md)

Follow the file order below. Type the comments too: they explain why the code exists. Before each checkpoint, predict its output.

## Step 1: define calculations

Type [calculator/__init__.py](../calculator/__init__.py), then [calculator/calculation.py](../calculator/calculation.py).

`Calculation` is an abstract parent: it stores `a` and `b` and requires `get_result()`. `Add` and `Subtract` inherit that structure and supply different implementations. An `Add` **is a** `Calculation`.

Run `python` to open Python's interactive prompt, then type:

```python
from calculator.calculation import Add, Subtract
calculations = [Add(10, 5), Subtract(20, 7)]
[calculation.get_result() for calculation in calculations]
```

**Checkpoint:** the result is `[15, 13]`. This is polymorphism: the same method call works with different calculation types. Try constructing `Calculation(10, 5)` after importing it; Python should raise `TypeError` because it is abstract. Leave the prompt with `exit()`.

**Explain it:** why does `Add` work without defining its own `__init__`?

## Step 2: give history ownership of its collection

Type [calculator/history.py](../calculator/history.py).

A `History` **has many** calculations. Its methods control collection changes, and callers receive a copy of the list. The copy still refers to the original calculation objects; it is not a deep copy.

In a new Python prompt:

```python
from calculator.calculation import Add, Subtract
from calculator.history import History
history = History()
history.add(Add(10, 5))
history.add(Subtract(20, 7))
history.remove(0).get_result()
len(history.get_history())
```

**Checkpoint:** the last two expressions produce `15` and `1`. Try `history.remove(-1)` and explain why this method rejects a negative index even though Python lists allow one. Leave the prompt with `exit()`.

## Step 3: connect the objects to a user

Type [calculator/cli.py](../calculator/cli.py) from top to bottom, then [calculator/__main__.py](../calculator/__main__.py).

The helper functions format calculations, display history, and read numbers. `run()` connects them in a **read–evaluate–print loop (REPL)**. Its dictionary maps command names to classes; calling the selected class creates a calculation object.

```bash
python -m calculator
```

| Command | Input to try | Expected behavior |
| --- | --- | --- |
| `add` | `10`, then `5` | Prints `Result: 15` and records the object. |
| `subtract` | `20`, then `7` | Prints `Result: 13` and records the object. |
| `history` | — | Lists both calculations, numbered 1 and 2. |
| `remove` | `1` | Removes the addition; subtraction becomes item 1. |
| `help` | — | Lists all six commands. |
| `exit` | — | Prints `Goodbye!` and ends the loop. |

**Checkpoint:** repeat with `pizza`, an invalid operand such as `hello`, and removal number `99`. The app should explain the mistake and accept another command. Start a fresh session and try `history` and `remove` while empty.

**Explain it:** where does the CLI convert a user's number to a Python index? Why must failed calculations stay out of history? How do `break`, `continue`, and `return` differ?

## Know the boundaries

History lasts only for the current session. Commands ignore surrounding whitespace and capitalization. Operands use floating-point arithmetic, which can have small rounding differences; `:g` gives compact display formatting. The CLI rejects NaN, infinity, and results outside the finite range. Ctrl+C or end-of-input exits cleanly.
