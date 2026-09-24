# Stage 6: Automate checks and transfer the design ideas

[Course home](https://github.com/kaw393939/is218-oop-calculator) · [Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/05-reliability) · [Completion criteria](https://github.com/kaw393939/is218-oop-calculator/blob/main/docs/assignment.md)

Run the complete suite on clean GitHub runners and explain how the design generalizes beyond this calculator.

**Start with [the lesson](docs/lessons/06-ci.md)**. It explains the file order, small checkpoints, experiments, and self-check questions. Use this branch as a worked reference beside the separate solution you are typing.

## Smaller checkpoints

Complete 6A (publish and diagnose CI) before 6B (design reflection). The lesson contains an annotated failure log and an independent README usability task.

Reference counts exclude your independent tasks; a higher passing count is expected when you keep those tests.

## Files added or changed

- [.github/workflows/tests.yml](.github/workflows/tests.yml)
- [docs/lessons/06-ci.md](docs/lessons/06-ci.md)

[Inspect changes from the previous stage](https://github.com/kaw393939/is218-oop-calculator/compare/learn/05-reliability...learn/06-ci).

## Verify this checkpoint

With dependencies installed and your virtual environment active, run from this project's root:

```bash
python -m pytest
python -m calculator
```

Expect **37 passing test cases** in this worked snapshot. The default test command enforces 100% line and branch coverage. Some tests cover multiple scenarios with loops; all 19 Stage 4 test functions remain unchanged.

## Stage boundary

This is the final worked reference. The application, tests, and pytest configuration are unchanged from Stage 5. Add your own README and reflection in your solution; optional extensions follow the completed baseline.

Explain this lesson's exit questions and restore any deliberate experiments before committing your solution and moving on. Shared course documents in this branch are a publication snapshot; the [current course home](https://github.com/kaw393939/is218-oop-calculator) carries later introductory updates.
