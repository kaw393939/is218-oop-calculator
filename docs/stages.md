# Work through the example branches

[Back to README](../README.md)

A branch is a named pointer to a Git commit. These seven teaching branches point to successive checkpoints on one development history. Each stage adds to the preceding stage; they are not seven copies of the finished code. `main` keeps the complete teaching guide on its own history.

## Easiest: read on GitHub, type in your own project

Open a branch from the [README table](../README.md#worked-example-branches). Read that branch's README, open the named files, and type them in your own project. Predict the checkpoint, run it, then explain the result before advancing. Your own work stays separate from the worked answers.

## Run the reference locally

Clone into a separate reference folder, not the folder where you type your solution:

```bash
git clone https://github.com/kaw393939/is218-oop-calculator.git calculator-reference
cd calculator-reference
git switch stage/00-setup
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows use `py -m venv .venv` and `.venv/Scripts/Activate.ps1` in PowerShell. The repository is private, so your GitHub account needs access to clone it.

To move forward in this reference clone:

```bash
git status
git switch stage/01-calculations
python -m pytest
```

Save edits before switching: Git can carry compatible local changes into another branch or refuse a conflicting switch. Use your separate solution folder for experiments. `git switch main` returns to the current finished guide. For a clone made before these branches existed, run `git fetch origin` first.

## Compare two adjacent stages

Each stage README links to its change comparison. You can also inspect changes locally:

```bash
git diff origin/stage/02-history..origin/stage/03-basic-cli -- calculator tests
```

This comparison shows the basic CLI and its tests arriving. Later, stage 04 replaces that small CLI with the complete one. Identify each added responsibility before typing the new code.

## What should pass at each stage?

| Stage | Verification | Expected scope |
| --- | --- | --- |
| 00 | `python -m pytest --version` | Tools installed. There are no tests yet; running bare pytest reports no tests. |
| 01 | `python -m pytest` | Arithmetic, abstraction, and polymorphism examples. |
| 02 | `python -m pytest` | Calculations plus history ownership and removal. |
| 03 | `python -m calculator` and `python -m pytest` | Four-command REPL; history is not connected yet. |
| 04 | `python -m calculator` and `python -m pytest` | All six commands and an automated history/removal session. |
| 05 | `python -m pytest` | Full 49-case suite, 100% line and branch coverage enforced. |
| 06 | `python -m pytest` and GitHub Actions | Same complete suite plus remote automation and documentation. |

For stages 01–04, explore missing paths with `python -m pytest --cov=calculator --cov-branch --cov-report=term-missing`. Partial coverage is expected while the tests grow. The strict final threshold first appears in stage 05.

Stage branches are worked answers at specific points, not a replacement for the lessons. The early tests are deliberately direct examples; stage 05 expands and reorganizes them into the full suite. The final stage has the same application, tests, and workflow as the finished version published with these lessons; subsequent maintenance on `main` may move ahead.
