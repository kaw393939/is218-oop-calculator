# Stage 2: introduce a shared calculation contract

[Previous lesson](01-objects.md) · [Worked branch](https://github.com/kaw393939/is218-oop-calculator/tree/learn/02-abstraction) · [Next lesson](03-history.md)

## Why this matters

The scratchpad now needs subtraction. Both operations store two operands and return a result. A shared contract lets the rest of the program ask either object the same question without learning its arithmetic.

## What you already have

Stage 1's Add object and four passing tests. Those behaviors should survive this refactoring: changing structure should not silently change addition.

## What you will add

You will define an abstract `Calculation`, specialize it as `Add` and `Subtract`, and use both polymorphically. An abstract class defines required behavior; it is not itself a usable arithmetic operation.

Update these files from the worked branch:

1. `calculator/calculation.py`: introduce the parent; move common initialization into it; make Add a subclass; add Subtract.
2. `tests/test_calculation.py`: preserve the original four examples and add subtraction, abstraction, and polymorphism checks.

[Compare this stage with Stage 1](https://github.com/kaw393939/is218-oop-calculator/compare/learn/01-objects...learn/02-abstraction).

## Type and run

Read the whole class relationship first. Then update `Calculation` and `Add` together before running: the parent must exist before the subclass can inherit from it. Run the original four tests to confirm the refactoring still works.

`ABC` and `@abstractmethod` require a concrete subclass to supply `get_result()`. The abstract method has a docstring but no arithmetic. Type hints such as `a: float` and `-> float` document expected inputs and output; Python does not automatically validate values from these hints.

Add Subtract and the new tests. In a fresh Python prompt:

```python
from calculator.calculation import Add, Subtract
calculations = [Add(10, 5), Subtract(20, 7)]
for calculation in calculations:
    print(calculation.get_result())
```

**Expect:** `15`, then `13`. After entering the loop body at `>>>`, press Enter on a blank line to execute the block. The caller uses one interface; each object supplies its implementation.

Try `from calculator.calculation import Calculation`, then `Calculation(10, 5)`. The resulting `TypeError` is expected. Exit Python and run:

```bash
python -m pytest
```

The worked stage has eight passing tests, including one that expects that exception.

## Explain and experiment

Temporarily change Subtract to add its inputs. Predict which test catches the bug, run the suite, and restore subtraction. The class still satisfies the required method name, but now violates its intended behavior. An abstract contract cannot replace assertions about correctness.

## Check your understanding

1. Why does Add no longer need its own initializer?
2. Why can the loop avoid `if type(calculation) == Add`?
3. Does using the right method name guarantee the right behavior?

<details>
<summary>Self-check after you explain</summary>

Add inherits the initializer from Calculation. Method lookup selects the implementation belonging to each receiving object, so the loop can stay uniform. The ABC enforces the presence of an implementation; meaningful tests check its behavior.

</details>

**Ready to move on:** eight tests pass and you can explain the mixed loop. Commit with `git add calculator tests` and `git commit -m "Stage 2: share a calculation contract"`.
