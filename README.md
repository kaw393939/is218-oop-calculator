# Stage 4: Connect the model to a happy-path REPL

[Course home](https://github.com/kaw393939/is218-oop-calculator) · [Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/03-history) · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/05-reliability)

Read commands, construct calculation objects, manage history, and print results. Automate successful conversations.

**Start with [the lesson](docs/lessons/04-repl.md)**. It explains the file order, small checkpoints, experiments, and self-check questions. Use this branch as a worked reference beside the separate solution you are typing.

## Smaller checkpoints

Start with [4A: arithmetic and exit](checkpoints/04a/README.md), then [4B: history and removal](checkpoints/04b/README.md). Both preserve 15 model tests. In 4C, add one CLI test for 16 cases, then the remaining tests for 19.

Reference counts exclude your independent tasks; a higher passing count is expected when you keep those tests.

## Files added or changed

- [calculator/cli.py](calculator/cli.py)
- [calculator/__main__.py](calculator/__main__.py)
- [tests/test_cli.py](tests/test_cli.py)

[Inspect changes from the previous stage](https://github.com/kaw393939/is218-oop-calculator/compare/learn/03-history...learn/04-repl).

## Verify this checkpoint

With dependencies installed and your virtual environment active, run from this project's root:

```bash
python -m pytest
python -m calculator
```

Expect **19 passing test cases** in this worked snapshot. The strict coverage gate comes in Stage 5; assertions begin now.

## Stage boundary

All six commands work with valid finite numbers and valid removal numbers. Invalid numeric input, out-of-range removal, and interrupted input can still raise exceptions. Reproduce one failure to motivate Stage 5; this is not the final reliability specification.

Explain this lesson's exit questions and restore any deliberate experiments before committing your solution and moving on. Shared course documents in this branch are a publication snapshot; the [current course home](https://github.com/kaw393939/is218-oop-calculator) carries later introductory updates.
