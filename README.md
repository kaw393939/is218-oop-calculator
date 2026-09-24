# Stage 00: Set up the project

This is the first stage. · [Next stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/01-calculations)

This branch is a worked checkpoint. Read it beside the separate project you are typing. [Full lessons and glossary](https://github.com/kaw393939/is218-oop-calculator/tree/main/docs) remain available on main.

## Type or update these files

- [.gitignore](.gitignore)
- [requirements.txt](requirements.txt)

Keep files from previous stages unless this stage replaces them. Read each comment and predict what the code will do before running it.

## Run the checkpoint

From this project's root, with dependencies installed in your active virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest --version
```

**Expected:** pytest reports its version. On Windows create the environment with `py -m venv .venv` and activate with `.venv/Scripts/Activate.ps1` in PowerShell.

**Not included yet:** Application files and tests. Bare pytest will report no tests at this stage.

**Explain before advancing:** Why keep the virtual environment out of Git?
