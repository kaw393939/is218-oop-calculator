# 2. Type and understand the calculator

[Previous: setup](01-setup.md) · [Next: testing](03-testing.md)

Follow the file order below. Type the comments too: they explain why the code exists. Before each checkpoint, predict its output.

## Why objects for something as small as addition?

Imagine keeping a scratchpad while checking scores for a game. Writing only `15` loses how you got there. `Add(10, 5)` keeps the operation and both inputs together; you can ask it for its result later. History is the scratchpad holding those calculation objects.

Two functions would be enough for basic addition and subtraction. We use objects here to practice grouping data with behavior and letting different operations share a contract. These choices become useful when a program grows.

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

### Slow down one line

For `calculation = Add(10, 5)`, Python creates an `Add` instance and calls its inherited initializer. Within that call, `self` refers to the new object, `a` is `10`, and `b` is `5`. `self.a = a` stores `10` on that particular object. Later, `calculation.get_result()` uses `Add`'s method and returns `15`.

Try `another = Add(100, 50)`. It has its own operands; it does not overwrite the first object's values. `Add` is the class; `calculation` and `another` refer to two instances.

The checkpoint's list comprehension is a compact version of this ordinary loop:

```python
results = []
for calculation in calculations:
    results.append(calculation.get_result())
print(results)
```

**Test now:** follow [your first test](03-testing.md#your-first-test) before building History. This gives you feedback while the program is still small.

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

The scratchpad analogy has a limit: these entries are live objects, not permanent receipts. The returned list is a copy, but the operands on its objects remain mutable. Try clearing a returned list and then reading history again. Why are the original entries still there?

## Step 3: connect the objects to a user

Type [calculator/cli.py](../calculator/cli.py) in two passes: first the imports, `HELP`, and helper functions through `read_number()`; then `run()`. Finish with [calculator/__main__.py](../calculator/__main__.py).

After the first pass, open a fresh Python prompt and try `from calculator.cli import describe`, `from calculator.calculation import Add`, and `describe(Add(10, 5))`. Expect `'Add: 10, 5 = 15'`. Exit Python before continuing. Restarting the prompt avoids using an older imported version of your edited file.

The helper functions format calculations, display history, and read numbers. `run()` connects them in a **read–evaluate–print loop (REPL)**. Its dictionary maps command names to classes; calling the selected class creates a calculation object.

Read `operations[command](a, b)` as two steps: select a class with `operation_class = operations[command]`, then create an object with `calculation = operation_class(a, b)`. For `add`, that second step is `Add(a, b)`.

Trace one request: **`add` → read `10` and `5` → create `Add` → validate result → store object in History → print `15` → wait for another command**. `get_result()` calculates on demand; History stores the object, not a cached answer.

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

Check your explanation: `break` leaves the nearest loop, `continue` starts its next iteration, and `return` leaves the current function. When input is invalid, this CLI returns to the command prompt; it does not keep asking for the same operand.

**Change one thing:** change a prompt's wording, run the app, then restore it. Predict whether arithmetic tests should care about that wording. This separates user-interface decisions from calculation behavior.

## Know the boundaries

History lasts only for the current session. Commands ignore surrounding whitespace and capitalization. Operands use floating-point arithmetic, which can have small rounding differences; `:g` gives compact display formatting. The CLI rejects NaN, infinity, and results outside the finite range. Ctrl+C or end-of-input exits cleanly.
