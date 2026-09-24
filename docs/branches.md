# Use the branches as worked checkpoints

[Course home](https://github.com/kaw393939/is218-oop-calculator)

## Choose the simple path first

Browse each `learn/...` branch on GitHub beside your own solution. Type into your own project continuously, staying on its `main` branch. You do not need to switch branches in your solution to complete this course.

Each worked branch contains the previous stage's code plus a focused increment. Its README identifies the lesson, source files, checkpoint, expected limitations, and the next stage. The lesson explains changes before asking you to type them. Tests begin in Stage 1.

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

- `main`: introduction, concepts, lessons, and instructor materials.
- `learn/01-objects` through `learn/06-ci`: the current six cumulative worked checkpoints, with linear ancestry between them.
- `learn/06-ci`: the completed calculator; the final application and tests are already present in Stage 5, and Stage 6 adds automation and reflection.
- `stage/...`: legacy references from the earlier course layout. They remain available for old links and are not part of this learning path.

Worked branches are published snapshots. The current course home may receive documentation improvements afterward. A maintainer must update a checkpoint explicitly when its code or lesson changes.
