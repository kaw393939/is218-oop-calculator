# Assignment and completion criteria

[Course home](https://github.com/kaw393939/is218-oop-calculator)

## Your task

Recreate the calculator by typing and understanding the six worked stages in your own repository. Use the examples as a reference, keep the same file structure, and commit your progress after each stage.

By the end, you should be able to:

- Construct objects and explain the difference between class, instance, attribute, and method.
- Explain why a second operation motivates a common abstract contract.
- Use inheritance and polymorphism without branching on each operation's type.
- Manage calculation objects through an encapsulated collection.
- Connect the model to a REPL and handle expected user mistakes.
- Assert behavior, investigate missing coverage, and automate checks.
- Explain which design ideas transfer to another language and which language rules still need study.

## Required final behavior

| Command | Acceptance example |
| --- | --- |
| `add` | Inputs 10 and 5 produce 15 and save an Add object. |
| `subtract` | Inputs 20 and 7 produce 13 and save a Subtract object. |
| `history` | Display operation names, operands, and results, numbered from 1. |
| `remove` | Remove a displayed entry and renumber the remaining entries. |
| `help` | Explain the six available commands. |
| `exit` | End the session cleanly. |

An empty history, unknown command, invalid operand, and invalid removal must not crash the final application. Failed calculations must not enter history. The reference also handles Ctrl+C, end-of-input, and nonfinite numeric values.

History is in memory for one session. The calculator uses Python floating-point numbers. Persistence, a web UI, exact-decimal accounting, and extra operations are outside the required scope.

## Evidence of completion

1. Your repository contains the application, meaningful tests, requirements, pytest configuration, and GitHub workflow.
2. `python -m calculator` supports the required session.
3. `python -m pytest` passes and enforces 100% line **and branch** coverage at the end of Stage 5.
4. Your Stage 6 workflow passes on Python 3.11–3.14.
5. Your README explains installation, running, testing, and the main design choices in your own words.
6. Your commit history records the six checkpoints. Include a short reflection answering the Stage 6 transfer questions.

The final reference has 37 test cases. Your test count may differ if you add meaningful cases; coverage alone is not proof of correctness. Do not remove behavior or exclude application code to reach the threshold.

## How understanding will be assessed

| Area | Evidence of understanding |
| --- | --- |
| Behavior | Demonstrate a successful session and recovery after invalid input. |
| OOP | Trace an object's state and explain abstraction, substitution, and collection ownership using your code. |
| Testing | Explain the claim made by an assertion and show a missing-path test. |
| Workflow | Reproduce the setup and explain a CI failure from its log. |
| Transfer | Describe a new operation or notification type without rewriting unrelated responsibilities. |

Optional extensions belong after the baseline passes. They should not replace required features or explanations.
