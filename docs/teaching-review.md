# Teaching review: reading this as a beginner

[Back to README](../README.md)

This is a walkthrough-based review from a beginner's perspective, not evidence from a student usability study. The code is small, responsibilities are separated, and the reference suite passes. The main instructional risk was that students could type the solution correctly while missing the reasons behind it.

## Findings and changes

| Priority | Where a student could get stuck | Improvement made |
| --- | --- | --- |
| High | “Why create classes just to add two numbers?” | Introduced a score-checking scratchpad: preserve operation and operands, then ask the object for its answer. Acknowledged that simple functions can solve basic arithmetic. |
| High | `self`, inherited initialization, and dictionary-selected construction appear too quickly. | Traced `Add(10, 5)` and expanded `operations[command](a, b)` into two conceptual steps. Explained the loop behind a comprehension. |
| High | Tests come after the entire application; parametrization hides the first basic assertion. | Added one temporary arrange–act–assert test immediately after calculations, including a deliberate failure and restoration. |
| High | Students can confuse the terminal, Python prompt, and editor. | Added explicit context instructions, prerequisites, common error explanations, and a fresh-interpreter reminder. |
| Medium | Typing the whole CLI postpones feedback for too long. | Split helpers from the REPL and added an independently runnable formatting checkpoint. |
| Medium | “Private” or “history” might imply stronger protection than the code offers. | Explained that underscores are conventions, list copies are shallow, operands are mutable, and results are calculated on demand. |
| Medium | `lambda`, fixtures, iterators, and unpacking compete with the OOP lesson. | Explained them as a scripted conversation and separated advanced supporting checks from the core concepts. |
| Medium | The project never says why these ideas matter beyond Python. | Added a sourced page on OOP history, patterns, SOLID, and transfer across languages, with limits to the grammar analogy. |

## Code observations worth teaching

`Calculation` is a useful contract, but its type hints do not validate operands at runtime. The CLI validates user input; direct callers must honor the numeric contract. `History.remove()` similarly documents an integer index and does not provide a complete validation layer for arbitrary external inputs.

History preserves calculation objects, not immutable audit records. Calling `get_result()` again recomputes the answer; mutating operands changes later results. A financial ledger or saved audit log would need different requirements. Those are discussion points, not extra features students must implement here.

The CLI is the densest file. Its nested error handling is reasonable for this exercise, but students should explain one successful command and one failed command before typing every branch. Detailed comments are appropriate for this reference; ask students eventually to explain the same code without reading them aloud.

## What to improve next with classroom evidence

- Ask a student to follow setup without help. Record the first unclear instruction rather than guessing which environment problem matters most.
- After each checkpoint, require a prediction and one small change. Successful transcription alone should not count as understanding.
- Use the [worked-example branches](stages.md) to pause at the basic CLI before adding history and removal. Observe whether that smaller checkpoint reduces confusion.
- For assessment, have students explain where multiplication belongs and where it does not. Ask for a new edge-case assertion rather than accepting coverage percentage alone.

The repository remains private. Students will need repository access or a distributed copy before they can use these lessons.
