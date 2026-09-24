# 1. Set up your project

[Back to README](../README.md) · [Next: build](02-build.md)

Use Python 3.11 or newer, Git, a terminal, and a text editor. Keep this reference repository open beside a **new, empty folder**. Type the files into that folder rather than copying the completed project.

You should already recognize variables, functions, `if`, loops, and lists. If those are unfamiliar, practice them first; OOP builds on them. You are learning to organize familiar operations around objects.

Commands marked `bash` belong in your terminal. Blocks marked `python` belong at Python's `>>>` prompt unless a lesson names a file. The prompt symbols are not part of what you type. Save each `.py` file in your editor before running it.

```bash
mkdir my-oop-calculator
cd my-oop-calculator
python3 -m venv .venv
source .venv/bin/activate
mkdir calculator tests
```

On Windows, use `py -m venv .venv` and activate with `.venv/Scripts/Activate.ps1` in PowerShell. The remaining Python commands are the same.

A virtual environment keeps this project's installed packages separate from other projects. Run all lesson commands from `my-oop-calculator`, with the environment active.

Type these reference files into the same paths in your project:

- [requirements.txt](../requirements.txt): the test tools and their allowed versions.
- [.gitignore](../.gitignore): files Git should leave out, including your environment and coverage reports.

Install the tools:

```bash
python -m pip install -r requirements.txt
```

The application needs no third-party packages. `pytest` runs tests; `pytest-cov` measures which application paths those tests execute.

**Checkpoint:** `python --version` reports 3.11 or newer, and `python -m pytest --version` succeeds. Create the application and test files in the next lessons.

## When something goes wrong

| What you see | What to check first |
| --- | --- |
| `SyntaxError` after typing a terminal command | You may be at `>>>`. Type `exit()` to return to the terminal. |
| `No module named calculator` | Run from the folder containing `calculator/`, not from inside it. Check filenames. |
| `No module named pytest` | Activate `.venv` and install `requirements.txt` with `python -m pip`. |
| `IndentationError` | Use four spaces per level; compare the indicated block with the source. |

Read the last line of a traceback for the error type, then find the line in your own file. Fix one issue and rerun. A typing mistake is useful feedback, not a reason to restart the project.
