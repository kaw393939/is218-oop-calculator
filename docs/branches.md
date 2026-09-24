# Use the branches as worked checkpoints

[Course home](https://github.com/kaw393939/is218-oop-calculator)

## Choose the simple path first

Browse each `learn/...` branch on GitHub beside your own solution. Type into your own project continuously, staying on its `main` branch. You do not need to switch branches in your solution to complete this course.

Each worked branch contains the previous stage's code plus a focused increment. Its README identifies the lesson, source files, checkpoint, expected limitations, and the next stage. The lesson explains changes before asking you to type them. Tests begin in Stage 1. Neighbor lesson links select the corresponding branch, so the instructions and source stay aligned.

## Run a reference locally when you need to compare behavior

Use a separate folder:

```bash
git clone https://github.com/kaw393939/is218-oop-calculator.git calculator-reference
cd calculator-reference
git switch learn/01-objects
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest
```

For Windows setup use the commands in [setup](setup.md). The repository is private; your GitHub account needs access, or your instructor must distribute a copy.

Before changing stages in the reference clone, run `git status`. Save any intended edits first. Git can carry compatible local changes across branches or refuse a switch with conflicts. Use your solution folder for experiments.

```bash
git fetch origin
git switch learn/02-abstraction
python -m pytest
```

`git switch main` returns to the course materials. Main has no calculator package or pytest suite: it is not the application checkpoint.

## Read the change, not just the finished file

Each stage after Stage 1 links to a GitHub comparison. In the reference clone you can also run:

```bash
git diff origin/learn/01-objects..origin/learn/02-abstraction -- calculator tests
```

Notice how the existing Add behavior survives the new parent class. Predict which tests should still pass before running them.

## Branch contract

- `main`: setup, assignment, concepts, glossary, shared readings, and instructor materials.
- `learn/01-objects` through `learn/06-ci`: six worked stages. Each contains cumulative application code and tests, its own lesson, and only its own intermediate checkpoints.
- `learn/06-ci`: the completed calculator; the final application and tests are already present in Stage 5, and Stage 6 adds automation and reflection.

Each stage builds on the preceding stage's code and shares its Git ancestry. Shared readings link back to `main`; lessons live on their matching branches. This keeps one maintained copy of each explanation.

## Intermediate checkpoints inside a stage

Stages 2, 4, and 5 include smaller worked examples in `checkpoints/` on their respective branches. Each folder explains exactly which source file to type into which file in your solution. These folders are references, not independent student projects: keep your existing files and run commands from your solution root. Do not copy the checkpoint directory wholesale.

The root of each learning branch remains the completed stage. Checkpoint files with names such as `cli_tests.py` are source references for `tests/test_cli.py`; their different names keep pytest from collecting intermediate reference code as extra tests.

Keep your earlier tests and independent tasks as you advance. The optional parametrization page is a later refactoring exercise, not permission to discard regression coverage.
