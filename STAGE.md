# Stage 06: Automate checks and finish the reference

[Previous stage](https://github.com/kaw393939/is218-oop-calculator/tree/stage/05-testing) · [Current main guide](https://github.com/kaw393939/is218-oop-calculator)

This branch is a worked checkpoint. Read it beside the separate project you are typing. [Full lessons and glossary](https://github.com/kaw393939/is218-oop-calculator/tree/main/docs) remain available on main.

[See exactly what changed](https://github.com/kaw393939/is218-oop-calculator/compare/stage/05-testing...stage/06-final).

## Type or update these files

- [.github/workflows/tests.yml](.github/workflows/tests.yml)
- [docs/04-github-actions.md](docs/04-github-actions.md)

Keep files from previous stages unless this stage replaces them. Read each comment and predict what the code will do before running it.

## Run the checkpoint

From this project's root, with dependencies installed in your active virtual environment:

```bash
python -m pytest
python -m calculator
```

**Expected:** 49 tests pass with 100% line and branch coverage. After pushing the workflow to your own repository, all four Python-version jobs should pass.

**Not included yet:** Nothing required by the assignment; optional extension ideas are in the lessons.

**Explain before advancing:** What does a clean GitHub runner verify that your existing local environment might hide?
