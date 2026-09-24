# Instructor guide

[Course home](https://github.com/kaw393939/is218-oop-calculator) · [Assignment](assignment.md)

## Design intent

Students build one application continuously while consulting six worked checkpoints. The sequence is concrete-first: introduce an object with observable behavior, then make a second operation create a reason for a shared abstraction. Testing begins with one direct assertion, not a parametrized matrix or a coverage target.

Main is the course home. It contains no completed calculator implementation. The `learn/...` branches carry the worked answers. The old `stage/...` branches are retained for compatibility and should not be assigned to new students.

## Facilitation and formative assessment

Treat each stage as a learning unit, not a mandatory time block. A beginner may need more than one session for the REPL or reliability stage. Advance when the learner can demonstrate and explain the checkpoint.

| Stage | Ask the learner to demonstrate | Listen for / likely misconception |
| --- | --- | --- |
| 1: Objects | Create two Add instances and inspect their operands. | `self` identifies an instance; it is not the class or a global variable. |
| 2: Abstraction | Run a mixed collection through `get_result()`. | A common contract permits different behavior; inheritance is not just copying code. |
| 3: History | Clear a returned list and show the internal history remains. | A shallow copy protects list membership, not the mutable objects it references. |
| 4: REPL | Trace one command from text to object to output. | Constructing an object and storing it are distinct actions; printing is not returning. |
| 5: Reliability | Read a traceback, add an assertion, inspect missing coverage. | Executed code is not necessarily correct; handling an exception must preserve valid state. |
| 6: CI / transfer | Interpret one workflow job and propose a new operation. | Shared design concepts do not imply identical syntax, types, or runtime rules. |

Use **predict → type → run → explain → change one thing**. Ask students to articulate their prediction before execution. A correct prediction with an imperfect explanation is a cue to probe, not a reason to assign more typing.

## Feedback rather than transcription

Each lesson has objectives, a motivating problem, a file order, runnable checkpoints, one small experiment, and exit questions with a collapsible self-check. The self-check is feedback after an attempt, not a replacement for an explanation in the student's own words.

During a demonstration, intentionally change an expected result so one test fails, then restore it. This shows that a green check means something was asserted. At Stage 5, demonstrate that the Stage 4 CLI has 100% coverage but still crashes on invalid text. Separate missing requirements from unexecuted code, then add recovery one test at a time. Install the coverage gate last. Parametrization is optional cleanup, not a required testing prerequisite.

The Stage 4 program intentionally assumes valid numeric input and valid removal numbers. Reproduce a failure there to motivate Stage 5. Do not grade Stage 4 as though it were the final specification.

## Use the smaller checkpoints

Stage 2A exposes duplicate initializers before 2B extracts the parent. Stage 4A runs arithmetic and exit, 4B connects history, and 4C introduces automated conversations. Stage 5A handles operands, 5B handles removal, and 5C finishes boundary checks before installing the coverage gate. Stage 6A publishes and interprets CI; 6B reflects on transferable design.

Each lesson has an independent task without a supplied implementation. Keep these tests when advancing; reference counts exclude student additions. The final reference preserves all 19 Stage 4 test functions unchanged and adds focused cases. Some new cases use familiar loops, so comparing its 37 function count to the old parametrized 49-case suite is not a quality metric.

Worked source under `checkpoints/` maps source filenames to target solution files. Students type the mapped code in their own project, not into the checkpoint folder. Instructor automation materializes each checkpoint from its recorded baseline and validates it separately; these checks do not count as student test cases.

## Assessment and pacing

Use the [assignment criteria](assignment.md) to assess behavior, explanation, testing, workflow, and transfer. A student should be able to add a new edge-case assertion and identify where a new operation belongs. Test count alone and memorized definitions are insufficient evidence.

Keep the history/patterns/SOLID reading optional until students can explain their own calculator. Stage 6 uses it to name ideas already encountered. The code illustrates some principles and similarities to patterns; it is not a comprehensive implementation of all patterns or all five SOLID principles.

No student usability study has been performed. Pilot setup with a student, record the first point where help is needed, and adjust pacing based on observations. The six-stage count is a design choice that should be evaluated with classroom evidence.

## Engineering and maintenance

Main's **Course checks** workflow validates local documentation paths and runs every current worked branch's tests on Python 3.14. Only Stage 6 introduces the student's **Calculator tests** workflow, which checks Python 3.11–3.14 and enforces the coverage requirement. Central reference checks are instructor infrastructure, not an extra early-stage student assignment.

To validate main locally, use `python tools/check_docs.py`. Main intentionally has no `pytest.ini`, `calculator/`, or `tests/` in its tracked tree. To test code, switch a separate reference clone to a learning branch.

When updating a stage, work in an isolated checkout, preserve earlier checkpoints, update its lesson and tests together, and propagate applicable changes forward through later stages. Avoid force-pushing shared teaching history. Recheck test counts, comparisons, and branch links before announcing a revision.

Worked checkpoints retain the shared course documents as of publication. Update main for ongoing introductory guidance; make an explicit checkpoint revision when a learner-facing code change is needed. Keep the legacy branches until you have deliberately communicated a retirement plan.

The repository is private. Arrange student access or distribute the materials before assigning the first lesson.
