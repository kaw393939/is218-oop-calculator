# Glossary

[Back to README](../README.md)

| Term | Meaning in this project |
| --- | --- |
| **Abstraction** | A shared promise about behavior: every calculation provides `get_result()`. |
| **Abstract base class (ABC)** | A parent class that can require methods in concrete subclasses. `Calculation` inherits from `ABC`. |
| **Abstract method** | A method marked `@abstractmethod`; a concrete subclass must implement it. |
| **Assertion** | A check of an expected fact, such as `assert result == 15`. |
| **Attribute** | Data attached to an object, such as `calculation.a`. |
| **Branch coverage** | Measurement of executed control-flow paths, such as both outcomes of a condition. |
| **Class** | A definition used to create objects with related data and behavior. |
| **CLI** | Command-line interface: the calculator's terminal commands and prompts. |
| **Collection** | A group of objects; history uses a list of calculations. |
| **Concrete class** | An instantiable class that supplies required behavior, such as `Add`. |
| **Continuous integration (CI)** | Automatically checking code changes with a repeatable build or test process. |
| **Decorator** | A function applied with `@` to modify or mark a definition, such as `@abstractmethod`. |
| **Dictionary** | A key/value mapping; `operations` maps command strings to classes. |
| **Docstring** | A string at the start of a module, class, or function describing its purpose. |
| **Edge case** | An unusual or boundary input, such as removing from empty history. |
| **Encapsulation** | Keeping responsibility for data and its management together behind methods. |
| **Exception** | A signal that interrupts normal execution; `try`/`except` handles expected errors. |
| **Fixture** | Test support supplied by pytest, such as `monkeypatch` or `capsys`. |
| **Float** | A floating-point number; decimal values may have small representation errors. |
| **GitHub Action** | A reusable workflow step, such as `actions/checkout`. |
| **Index** | An element's position in a collection; Python lists start at zero. |
| **Inheritance** | Deriving a class from another; `Add` inherits from `Calculation`. |
| **Initializer** | `__init__`, called to initialize an instance's state after creation. |
| **Instance / object** | A particular value created from a class, such as `Add(10, 5)`. |
| **Job** | A set of workflow steps executed on a runner. |
| **Line coverage** | Measurement of which executable lines the tests reached. |
| **List comprehension** | An expression that builds a list by iterating, such as `[c.get_result() for c in calculations]`. |
| **Matrix** | Workflow configuration that repeats a job for multiple values, here Python versions. |
| **Method** | A function defined on a class, such as `History.remove()`. |
| **Module** | An importable Python file, such as `history.py`. |
| **Operand** | An input to an operation; `a` and `b` are operands. |
| **Package** | A collection of Python modules; this regular package includes `__init__.py`. |
| **Parametrization** | Running a test with multiple sets of input and expected values. |
| **Polymorphism** | Calling one interface on different objects and receiving their specific behavior. |
| **REPL** | Read, evaluate, print, loop: the calculator's repeated interaction cycle. |
| **Runner** | The machine that executes a GitHub Actions job. |
| **self** | The conventional name for the instance a method operates on. |
| **Shallow copy** | A new container holding references to the same contained objects. |
| **State** | Data held at a particular moment, such as the entries currently in history. |
| **Type hint** | An annotation documenting an expected type; Python does not automatically enforce it. |
| **Virtual environment** | An isolated Python environment for a project's installed packages. |
| **Workflow** | A YAML file defining automated triggers, jobs, and steps. |
| **YAML** | The indentation-based configuration format used for GitHub workflows. |

## The bigger picture

See [OOP across languages](05-oop-across-languages.md) for examples and context.

| Term | Plain-language meaning |
| --- | --- |
| **Aggregation** | A relationship where a collection refers to objects that can exist independently, as History does. |
| **Composition** | Building behavior from collaborating objects; in strict UML usage, a stronger ownership/lifetime relationship. |
| **Contract** | The operations and behavioral promises that callers can rely on. |
| **Dependency** | Something another part of a program needs to perform its work. |
| **Dependency injection** | Providing a dependency from outside instead of constructing it inside its user. |
| **Design pattern** | A named approach to a recurring design problem, including its tradeoffs. |
| **Duck typing** | Using an object based on supported behavior rather than requiring a particular inheritance relationship. |
| **Interface** | The capabilities available to a caller; some languages also have an explicit `interface` construct. |
| **Prototype** | An object from which another object can inherit properties or behavior, as in JavaScript. |
| **Semantics** | What a language construct means or does. |
| **SOLID** | Five principles for thinking about responsibilities, extensions, contracts, interfaces, and dependencies. |
| **Subtype** | A type whose values should be usable where the more general type is expected, honoring its contract. |
| **Syntax** | The spelling and structural rules for valid code in a language. |
