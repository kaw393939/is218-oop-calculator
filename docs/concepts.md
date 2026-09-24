# Concepts to recognize as you build

[Course home](https://github.com/kaw393939/is218-oop-calculator) · [Glossary](glossary.md)

Imagine checking scores on a scratchpad. Writing only `15` loses the inputs and operation. An `Add(10, 5)` object keeps that information together and can calculate its result. History becomes the collection of entries.

Simple functions could perform the arithmetic. This project uses objects so you can practice assigning responsibilities and introducing a shared contract when a second operation arrives.

| Stage | Familiar question | Programming concept |
| --- | --- | --- |
| 1 | Which entry am I asking about? | An **object** has its own state; a **class** describes how to create and use such objects. |
| 1 | What can this entry do? | A **method** provides behavior, using that object's attributes. |
| 2 | What can I ask every kind of calculation? | **Abstraction** provides a common contract. |
| 2 | How can an operation specialize that contract? | **Inheritance** gives a subclass a relationship to a base class. |
| 2 | Can I make the same request of different operations? | **Polymorphism** lets each object answer through its implementation. |
| 3 | Who should manage the collection? | **Encapsulation** puts collection management behind History's methods. |
| 4 | How do these parts cooperate with a person? | A **REPL** reads a command, evaluates it, prints feedback, and repeats. |
| 5 | Which paths have I overlooked? | **Coverage** identifies unexecuted code; assertions check expected behavior. |
| 6 | Does it work in a fresh environment? | **Continuous integration** automatically repeats the checks. |

## Two relationships to keep distinct

```text
Calculation             History
  ├── Add                  └── stores calculation objects
  └── Subtract

Add IS A Calculation.   History HAS calculations.
```

These relationships appear gradually. Stage 1 has only `Add`; do not introduce the whole diagram before you understand one object.

## Follow one request

By Stage 4, `add` leads to: read operands → create an Add object → store it through History → print its result → read another command. Stage 5 adds checks so rejected input never enters history.

Ask three questions when reading any file: **What does this part know? What is it responsible for? What should it leave to another part?** The answers matter more than memorizing the terminology.

The scratchpad analogy has a limit: history holds live calculation objects, not immutable receipts. Changing an operand changes a later computed result. A list copy protects collection membership, not all data inside each object.
