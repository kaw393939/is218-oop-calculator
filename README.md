# Stage 2: Abstraction, inheritance, and polymorphism

[Course home](https://github.com/kaw393939/is218-oop-calculator) · [Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/01-objects) · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/03-history)

Introduce Calculation only after a second operation gives us a reason for a shared contract.

**Start with [the lesson](docs/lessons/02-abstraction.md)**. It explains the file order, small checkpoints, experiments, and self-check questions. Use this branch as a worked reference beside the separate solution you are typing.

## Files added or changed

- [calculator/calculation.py](calculator/calculation.py)
- [tests/test_calculation.py](tests/test_calculation.py)

[Inspect changes from the previous stage](https://github.com/kaw393939/is218-oop-calculator/compare/learn/01-objects...learn/02-abstraction).

## Verify this checkpoint

With dependencies installed and your virtual environment active, run from this project's root:

```bash
python -m pytest
```

Expect **8 passing test cases** in this worked snapshot. The strict coverage gate comes in Stage 5; assertions begin now.

## Stage boundary

The model supports addition and subtraction. There is no history collection or user interface yet. Original addition tests remain as regression checks.

Explain this lesson's exit questions and restore any deliberate experiments before committing your solution and moving on. Shared course documents in this branch are a publication snapshot; the [current course home](https://github.com/kaw393939/is218-oop-calculator) carries later introductory updates.
