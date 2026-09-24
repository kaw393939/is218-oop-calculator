# 5. OOP is a language you can carry with you

[Previous: GitHub Actions](04-github-actions.md) · [Glossary](glossary.md) · [Back to README](../README.md)

You are learning more than how to write a Python calculator. You are learning how to assign responsibilities, describe relationships, and let parts of a program collaborate. Those questions will follow you into other languages and much larger applications.

Read this after building the calculator. The examples below are explanations and optional exercises, not additional required application files.

## Think of it as learning grammar

When learning another human language, recognizing an action, its subject, and its object helps you understand an unfamiliar sentence. OOP gives you a similar set of questions for reading a program:

| Read this code | Say it in ordinary language | Recognize the idea |
| --- | --- | --- |
| `Add(10, 5)` | Create one addition with these two inputs. | An object combines state and behavior. |
| `calculation.get_result()` | Ask this calculation for its answer. | A method provides an interface to behavior. |
| `class Add(Calculation)` | Addition is a kind of calculation. | Inheritance expresses a subtype relationship. |
| `history.add(calculation)` | Ask history to manage another entry. | Objects collaborate through public methods. |
| `get_result()` on either subclass | Make the same request and let the object supply the behavior. | Polymorphism. |

**Syntax** is how a language spells these expressions. **Semantics** is what they mean. Design is how you choose to organize them. Calling OOP “grammar” is a learning analogy: it gives you reusable ways to read and build programs, but it is not one literal grammar shared by every language.

For example, a music app can ask a local track or streamed track to `play()`. The caller wants playback; each implementation handles its own details. That is the same *kind of design question* as asking both `Add` and `Subtract` for `get_result()`.

## Where these ideas came from

| Milestone | The problem and the lasting idea |
| --- | --- |
| **1960s: Simula** | Ole-Johan Dahl and Kristen Nygaard developed Simula around simulation. Modeling a system as interacting entities helped establish classes, objects, and inheritance. See the research retrospective [Object-oriented programming: some history](https://arxiv.org/abs/1303.0427). |
| **1970s: Smalltalk** | Alan Kay and colleagues at Xerox PARC explored interactive computing using communicating objects. Messaging and each object's own behavior were central, not just class hierarchies. Kay recounts this work in [The Early History of Smalltalk](https://doi.org/10.1145/155360.155364). |
| **1994: a shared pattern vocabulary** | Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides published a catalog of 23 recurring object-oriented designs. Their [Design Patterns](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-software-9780201633610) book helped programmers discuss designs by name. |
| **Later design guidance: SOLID** | Principles developed by several contributors became widely taught together as SOLID. Robert C. Martin's [discussion of the principles](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html) focuses on managing dependencies and change. They guide design; they are not language features. |

These ideas accumulated through experience. OOP, patterns, and SOLID are related layers of knowledge, not inventions from one person or one moment.

## What transfers when the language changes?

The first thing to look for is the contract: what can a caller ask this object to do? Then look for the state it owns and the implementation that answers the request.

| Language | Familiar idea, different expression | A difference to learn |
| --- | --- | --- |
| **Python** | `class Add(Calculation)` and `get_result()` | This project uses an ABC. Python also supports cooperation based on available behavior, often called duck typing. `_name` signals internal use by convention. See the [Python class tutorial](https://docs.python.org/3/tutorial/classes.html). |
| **Java** | Classes can extend a parent and implement interfaces. | Class inheritance and interface implementation have different roles. See [Java inheritance](https://dev.java/learn/inheritance/). |
| **C#** | A base type can define a method that subclasses override. | `abstract`, `virtual`, and `override` explicitly control these relationships. See [C# polymorphism](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/polymorphism). |
| **JavaScript** | Classes and methods can express similar collaborations. | Objects use prototype-based inheritance underneath class syntax. See [MDN's class guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes). |

For reading practice, these expressions all mean “ask this object for its result,” assuming the respective class defines that method:

```text
Python:       calculation.get_result()
Java:         calculation.getResult();
C#:           calculation.GetResult();
JavaScript:   calculation.getResult();
```

Method names here illustrate common conventions, not required keywords. They are expressions, not complete runnable programs.

The same questions also help with C++, Ruby, Kotlin, Swift, and other languages supporting object-oriented designs. You still need to learn each language's rules for types, object lifetime, visibility, inheritance, and errors. Some emphasize protocols, interfaces, or prototypes. Learning Python OOP gives you a foundation for those differences, not automatic fluency in all of them.

## Design patterns: names for recurring solutions

A pattern describes a recurring problem, an arrangement of responsibilities, and its tradeoffs. Think of a familiar essay structure: it helps organize your writing, but it does not supply every sentence. The pattern catalog distinguishes creation, structure, and behavior problems. [Design Patterns publisher overview](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-software-9780201633610).

Here are connections to our calculator. These are teaching comparisons, not a claim that the project implements every named pattern.

| Pattern or technique | Relatable situation | Connection and limit |
| --- | --- | --- |
| **Strategy** | A route planner chooses walking or driving directions through a shared request. | Our operations share a result interface. That resembles interchangeable behavior, but the app does not have a separate context holding a replaceable strategy. |
| **Command** | An editor represents a user request as an object that can be queued or saved. | A calculation packages an operation and its operands. We have no general command executor or undo behavior. Removing a history entry is not undoing a state-changing command. |
| **Factory-style selection** | A menu choice determines which kind of item gets created. | `operations[command](a, b)` chooses a class and constructs it. This simple dictionary is not the formal Factory Method pattern, which delegates creation through an overridable method. |

You do not earn better design by adding more patterns. First identify an actual problem, then ask whether the pattern solves it more clearly than the simpler code.

## SOLID: five questions to ask when changing code

The definitions below summarize established principles; the calculator comparisons are our own application of them. See [Martin's explanation](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html).

| Principle | Question in plain language | Apply it to this project |
| --- | --- | --- |
| **S — Single Responsibility** | Are things that change for different reasons separated? | Changing a terminal prompt belongs in the CLI, not in `Add`. History owns collection management. This does not mean every class has one method. |
| **O — Open/Closed** | Can I add a behavior without rewriting stable users of it? | A future `Multiply` could work with existing history and display. The operation imports, command dictionary, help, and tests still need updates; the whole app is not closed to every change. |
| **L — Liskov Substitution** | Does a replacement honor the behavior callers expect? | A subclass whose `get_result()` returns text or unexpectedly clears history would break the intended contract. Having the right method name alone is insufficient. |
| **I — Interface Segregation** | Must a caller depend on capabilities it does not need? | Calculations need an arithmetic interface, not required methods for printing menus or saving files. A small contract lets different callers use the relevant behavior. |
| **D — Dependency Inversion** | Do important policies depend on abstractions rather than storage or UI details? | History imports `Calculation`, not each operation subclass. The CLI still constructs concrete classes; a future storage abstraction could separate session behavior from file/database details if needed. |

A contract includes behavior as well as method names. Here, callers expect a numeric result without changing history; the CLI additionally expects the operands `a` and `b` for display. Python's ABC enforces the required method's presence, not all these expectations. Tests help check them.

For an everyday analogy to dependency inversion, imagine organizing a delivery around “send this notification” rather than a specific phone model. You agree on the capability and supply a suitable implementation. **Dependency injection** means supplying a dependency from outside; it can support inversion, but passing an object as an argument does not by itself guarantee good dependency design.

## Prefer the relationship that fits

`Add` **is a** `Calculation`. `History` **has** calculations. History should not inherit from Calculation just to reuse its code: a collection cannot sensibly substitute for one arithmetic operation.

Building with collaborating objects is often called composition. More strictly, UML distinguishes composition from aggregation based on ownership and lifetime. Our history stores references to independently created calculations, so it is not an example of exclusive lifetime ownership.

Use inheritance when the subtype can honor the parent's contract. Use collaborating objects when one responsibility needs another. OOP can also work alongside functions and other programming styles; our CLI already uses ordinary functions.

## Prove that the idea transfers

1. **Explain:** why can History store a new operation without learning its arithmetic?
2. **Predict:** for an optional `Multiply`, list every file that would change before writing any code. Include registration, help, and tests.
3. **Transfer:** imagine `EmailNotification` and `TextNotification`, each with `send()`. What should the caller rely on? What must both implementations promise?

You have understood the shared “grammar” when you can explain those responsibilities without depending on Python's spelling. Then a new language becomes a search for how it expresses familiar ideas, plus an investigation of where its rules differ.
