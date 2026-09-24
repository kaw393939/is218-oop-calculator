# Stage 2: discover why a shared contract helps

[Previous lesson](https://github.com/kaw393939/is218-oop-calculator/blob/learn/01-objects/docs/lessons/01-objects.md) · [Worked branch](https://github.com/kaw393939/is218-oop-calculator/tree/learn/02-abstraction) · [Next lesson](https://github.com/kaw393939/is218-oop-calculator/blob/learn/03-history/docs/lessons/03-history.md)

## Why this matters

The scratchpad now needs subtraction. Before introducing a parent class, build two concrete operations and notice what they have in common. Abstraction answers a problem you have seen, rather than appearing as a rule to memorize.

## What you already have

One Add class and four passing reference tests. Keep your independent test too. The existing behavior must survive each change.

## What you will add

Two checkpoints: **2A, separate concrete classes → 2B, a shared parent and polymorphic use**. Type hints are supporting notation; inheritance and the behavioral contract are the main ideas.

[Compare this stage with Stage 1](https://github.com/kaw393939/is218-oop-calculator/compare/learn/01-objects...learn/02-abstraction).

## Type and run

### 2A — Add the second concrete operation

Open [Checkpoint 2A](https://github.com/kaw393939/is218-oop-calculator/tree/learn/02-abstraction/checkpoints/02a). Its table maps worked-source filenames to the files in your solution. Type the two classes into `calculator/calculation.py`, keep your original tests, and add the two subtraction examples to `tests/test_calculation.py`.

Run `python -m pytest`: **six reference cases pass**. No abstract class or decorators are needed yet.

Compare the initializers. Both store `a` and `b` in exactly the same way. The result methods differ. Circle the shared responsibility before moving it.

### 2B — Refactor without changing those results

Now use the root [calculation.py](https://github.com/kaw393939/is218-oop-calculator/blob/learn/02-abstraction/calculator/calculation.py). Update the parent and both subclasses together: `Calculation` owns initialization, and `Add` and `Subtract` inherit it. Their result methods stay specialized.

Run your six existing tests **before adding more tests**. They should still pass. This is a refactoring checkpoint: changed organization, preserved behavior.

`ABC` and `@abstractmethod` require concrete subclasses to implement `get_result()`. A docstring is a valid method body, but this abstract method provides no arithmetic. Type hints such as `a: float` and `-> float` document expectations; they do not enforce numeric validation at runtime. `-> None` means the initializer does not return a result value to its caller.

Add the abstraction and polymorphism tests from the root [test file](https://github.com/kaw393939/is218-oop-calculator/blob/learn/02-abstraction/tests/test_calculation.py). In a fresh Python prompt:

```python
from calculator.calculation import Add, Subtract
calculations = [Add(10, 5), Subtract(20, 7)]
for calculation in calculations:
    print(calculation.get_result())
```

**Expect:** `15`, then `13`. At `>>>`, press Enter on a blank line after the loop body. The caller asks one question; each object supplies its implementation.

Import `Calculation` and try constructing it. The `TypeError` is expected. In a test, `with pytest.raises(TypeError):` means the indented operation is supposed to raise that exception; pytest fails the test if it does not.

Exit Python and run `python -m pytest`: **eight reference cases pass**, plus your own additions.

## Explain and experiment

Temporarily make Subtract add its operands. Predict which existing test fails, run it, and restore subtraction. A required method name cannot guarantee correct behavior.

### Build something independently

Create a test containing three calculations with numbers you choose, including a subtraction with a negative result. Use one ordinary loop to collect results. Assert the complete expected list without checking the objects' types inside the loop. Keep this test.

## Check your understanding

1. Which responsibility moved into Calculation, and which stayed in the subclasses?
2. Why did the six existing tests still work after the refactoring?
3. Why can a caller use `get_result()` without identifying the subclass first?

<details>
<summary>Self-check after you explain</summary>

The parent owns operand initialization and the common method contract. Each subclass owns its arithmetic. The public behavior remained stable, so the earlier assertions still apply. Method lookup selects the receiving object's implementation, allowing a uniform loop.

</details>

**Ready to move on:** explain the duplicated code you removed, pass the eight reference cases and your additions, and commit the stage. Do not delete earlier independent tests when consulting the new worked file.
