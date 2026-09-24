# 1. Set up your project

[Back to README](../README.md) · [Next: build](02-build.md)

Use Python 3.11 or newer, Git, a terminal, and a text editor. Keep this reference repository open beside a **new, empty folder**. Type the files into that folder rather than copying the completed project.

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
