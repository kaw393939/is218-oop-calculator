# Stage 06: Finished worked example

[Read this stage’s checkpoint and changes](STAGE.md).

# Build an OOP Calculator

[![Tests](https://github.com/kaw393939/is218-oop-calculator/actions/workflows/tests.yml/badge.svg)](https://github.com/kaw393939/is218-oop-calculator/actions/workflows/tests.yml)

An IS218 guided project: recreate a Python calculator by typing the commented source into your own project. Learn how objects, inheritance, a terminal interface, and automated tests work together.

## Follow the lessons in order

1. [Set up your project](docs/01-setup.md)
2. [Type and understand the calculator](docs/02-build.md)
3. [Test behaviors and investigate coverage](docs/03-testing.md)
4. [Run tests automatically with GitHub Actions](docs/04-github-actions.md)
5. [See the bigger picture: OOP history, patterns, SOLID, and other languages](docs/05-oop-across-languages.md)

Keep the [glossary](docs/glossary.md) nearby. Read the comments, type each file, and run each checkpoint before moving on.

Use **predict → type → run → explain → change one thing**. Lesson 5 is a conceptual reading; you do not need to memorize its terminology to build the calculator. Instructors can read the [student-perspective review](docs/teaching-review.md).

**Finished app:** `add`, `subtract`, `history`, `remove`, `help`, `exit`.

**Finish line:** working CLI, meaningful tests, 100% line and branch coverage, and a passing GitHub Actions run in your own repository.

## Worked-example branches

Each branch is a runnable checkpoint, building on the previous one. Use it as a reference beside the separate project you are typing. `main` contains the complete guide and current finished application.

| Branch | What you build |
| --- | --- |
| [stage/00-setup](https://github.com/kaw393939/is218-oop-calculator/tree/stage/00-setup) | Project files, environment, and test dependencies. No application yet. |
| [stage/01-calculations](https://github.com/kaw393939/is218-oop-calculator/tree/stage/01-calculations) | Abstract Calculation, Add, Subtract, and first assertions. |
| [stage/02-history](https://github.com/kaw393939/is218-oop-calculator/tree/stage/02-history) | Encapsulated history, removal, and collection tests. |
| [stage/03-basic-cli](https://github.com/kaw393939/is218-oop-calculator/tree/stage/03-basic-cli) | A small REPL with arithmetic, help, exit, and input handling. |
| [stage/04-complete-cli](https://github.com/kaw393939/is218-oop-calculator/tree/stage/04-complete-cli) | All six commands, with saved calculations and safe removal. |
| [stage/05-testing](https://github.com/kaw393939/is218-oop-calculator/tree/stage/05-testing) | Full automated suite and a 100% line/branch coverage gate. |
| [stage/06-final](https://github.com/kaw393939/is218-oop-calculator/tree/stage/06-final) | Finished reference with GitHub Actions and all lessons. |

Read [how to browse, run, and compare stages](docs/stages.md). Each branch's README states what to type, what to run, and what is intentionally unfinished.
