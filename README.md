# Stage 1: Objects, state, methods, and first assertions

[Course home](https://github.com/kaw393939/is218-oop-calculator) · [Setup](https://github.com/kaw393939/is218-oop-calculator/blob/main/docs/setup.md) · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/02-abstraction)

Build one concrete Add class, create independent instances, and verify their behavior.

**Start with [the lesson](docs/lessons/01-objects.md)**. It explains the file order, small checkpoints, experiments, and self-check questions. Use this branch as a worked reference beside the separate solution you are typing.

## Smaller checkpoints

The lesson includes a two-instance diagram and an independent test to write. Keep that test as you advance.

Reference counts exclude your independent tasks; a higher passing count is expected when you keep those tests.

## Files added or changed

- [calculator/__init__.py](calculator/__init__.py)
- [calculator/calculation.py](calculator/calculation.py)
- [tests/test_calculation.py](tests/test_calculation.py)

## Verify this checkpoint

With dependencies installed and your virtual environment active, run from this project's root:

```bash
python -m pytest
```

Expect **4 passing test cases** in this worked snapshot. The strict coverage gate comes in Stage 5; assertions begin now.

## Stage boundary

There is no abstract parent, subtraction, history, or terminal interface yet. Type hints and pytest parametrization are not needed for these first examples.

Explain this lesson's exit questions and restore any deliberate experiments before committing your solution and moving on. Shared course documents in this branch are a publication snapshot; the [current course home](https://github.com/kaw393939/is218-oop-calculator) carries later introductory updates.
