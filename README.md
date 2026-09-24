# Learn OOP by Building a Calculator

Start with one object. Grow it into a tested, interactive application. Learn the design ideas you can carry into other programming languages.

**This default branch is the course home, not the finished calculator.** Read the reference, then type your solution in a separate project. [Set up your workspace](docs/setup.md) first.

<details>
<summary>See the calculator you will build</summary>

```text
> add
First number: 10
Second number: 5
Result: 15
> history
Calculation History

1. Add: 10, 5 = 15
> exit
Goodbye!
```

History remembers the operation and inputs, not just the answer. The six stages build toward this interaction.

</details>

## Your learning path

| Stage | Worked-example branch | What you will be able to do |
| --- | --- | --- |
| 1 | [Objects and methods](https://github.com/kaw393939/is218-oop-calculator/tree/learn/01-objects) | Create an `Add` object and test its behavior. |
| 2 | [A shared calculation contract](https://github.com/kaw393939/is218-oop-calculator/tree/learn/02-abstraction) | Use inheritance and polymorphism to support different operations. |
| 3 | [History and encapsulation](https://github.com/kaw393939/is218-oop-calculator/tree/learn/03-history) | Manage a collection through a responsible object's methods. |
| 4 | [An interactive calculator](https://github.com/kaw393939/is218-oop-calculator/tree/learn/04-repl) | Connect objects through a read–evaluate–print loop. |
| 5 | [Errors, tests, and coverage](https://github.com/kaw393939/is218-oop-calculator/tree/learn/05-reliability) | Handle mistakes and use missing coverage to investigate behavior. |
| 6 | [CI and design reflection](https://github.com/kaw393939/is218-oop-calculator/tree/learn/06-ci) | Automate checks and explain how this design transfers. |

Each branch contains the cumulative worked code, tests, and its lesson. Follow **predict → type → run → explain → change one thing**. [How the branches work](docs/branches.md).

## Keep nearby

- [Assignment and completion criteria](docs/assignment.md)
- [Core concepts](docs/concepts.md) and [glossary](docs/glossary.md)
- [The bigger picture: OOP history, patterns, SOLID, and other languages](docs/bigger-picture.md) — revisit after Stage 6
- [Instructor guide](docs/instructor-guide.md)

**Finished application:** `add`, `subtract`, `history`, `remove`, `help`, `exit`. **Evidence:** meaningful assertions, 100% line and branch coverage, and passing GitHub Actions checks.
