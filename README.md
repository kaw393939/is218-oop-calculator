# Stage 3: Encapsulate a collection of calculations

[Course home](https://github.com/kaw393939/is218-oop-calculator) · [Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/02-abstraction) · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/04-repl)

Give History responsibility for storing and removing objects without exposing its internal list directly.

**Start with [the lesson](docs/lessons/03-history.md)**. It explains the file order, small checkpoints, experiments, and self-check questions. Use this branch as a worked reference beside the separate solution you are typing.

## Smaller checkpoints

The lesson pairs a two-list diagram with both list-clearing and object-mutation experiments. Write your own empty-history test before advancing.

Reference counts exclude your independent tasks; a higher passing count is expected when you keep those tests.

## Files added or changed

- [calculator/history.py](calculator/history.py)
- [tests/test_history.py](tests/test_history.py)

[Inspect changes from the previous stage](https://github.com/kaw393939/is218-oop-calculator/compare/learn/02-abstraction...learn/03-history).

## Verify this checkpoint

With dependencies installed and your virtual environment active, run from this project's root:

```bash
python -m pytest
```

Expect **15 passing test cases** in this worked snapshot. The strict coverage gate comes in Stage 5; assertions begin now.

## Stage boundary

The model handles invalid collection requests by raising exceptions. A user interface will translate requests in Stage 4 and handle numeric/removal mistakes in Stage 5.

Explain this lesson's exit questions and restore any deliberate experiments before committing your solution and moving on. Shared course documents in this branch are a publication snapshot; the [current course home](https://github.com/kaw393939/is218-oop-calculator) carries later introductory updates.
