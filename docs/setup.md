# Before Stage 1: set up your workspace

[Course home](https://github.com/kaw393939/is218-oop-calculator) · [Next: Stage 1](https://github.com/kaw393939/is218-oop-calculator/tree/learn/01-objects)

## What you need

Use Python 3.11 or newer, Git, a terminal, and a text editor. You should recognize variables, functions, conditions, loops, and lists. No prior classes, abstract classes, pytest, or GitHub Actions knowledge is required.

Keep this repository open as your reference. Create a **separate empty folder** for the solution you will type. Do not clone the completed code into your solution folder.

## Create and activate the environment

On macOS or Linux, type these commands in your terminal:

```bash
mkdir my-oop-calculator
cd my-oop-calculator
python3 -m venv .venv
source .venv/bin/activate
mkdir calculator tests
```

On Windows PowerShell:

```powershell
mkdir my-oop-calculator
cd my-oop-calculator
py -m venv .venv
.venv/Scripts/Activate.ps1
mkdir calculator
mkdir tests
```

A virtual environment keeps installed packages separate from other projects. Activate it again when opening a new terminal. Run project commands from the folder containing `calculator/` and `tests/`.

Type [requirements.txt](../requirements.txt) and [.gitignore](../.gitignore) into files with those names in your solution folder, then run:

```bash
python -m pip install -r requirements.txt
python --version
python -m pytest --version
```

**Checkpoint:** Python reports 3.11 or newer and pytest reports its version. There is no calculator or test suite yet. Running bare pytest now reports no tests; that is expected.

## Know where to type

| Context | What belongs there |
| --- | --- |
| Terminal | Commands such as `python -m pytest` and `git status`. |
| Python prompt (`>>>`) | Short Python experiments after you run `python`. Type `exit()` to return to the terminal. |
| Editor | Named `.py`, `.ini`, and `.yml` files. Save before running. |

Do not type prompt symbols. Lesson experiments name their context. Restart the Python prompt after editing imported files so you do not inspect an older loaded version.

## Start your own history

In your solution folder:

```bash
git init -b main
git add .gitignore requirements.txt
git commit -m "Set up calculator project"
```

If Git asks for your identity, configure your name and email as instructed by your course before retrying. Commit after each successful stage; your solution stays on its own `main` branch.

## Troubleshooting

| Symptom | First check |
| --- | --- |
| `SyntaxError` after a terminal command | You may be at `>>>`; type `exit()` first. |
| `No module named calculator` | Check the working folder, saved files, and spelling. |
| `No module named pytest` | Activate the environment and install requirements with `python -m pip`. |
| `IndentationError` | Compare indentation; use four spaces per level. |
| Import still shows old behavior | Restart the Python prompt after editing the module. |

Read the final line of a traceback, locate the named line in your file, and fix one issue at a time. If something remains unclear, record the command, exact error, and what you expected.
