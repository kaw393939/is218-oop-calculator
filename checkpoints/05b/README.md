# Checkpoint 05B

[Read the lesson](../../docs/lessons/05-reliability.md). This folder contains worked source for one intermediate checkpoint.

**Type the source into the target files in your solution folder.** Keep the other files you already built. These are reference fragments, not a separate project; run commands from your solution root.

| Worked source | Target in your solution |
| --- | --- |
| [cli.py](cli.py) | `calculator/cli.py` |
| [cli_tests.py](cli_tests.py) | `tests/test_cli.py` |

Run `python -m pytest`: the unextended reference has **23 passing tests**. Then run `python -m calculator` and follow the lesson conversation.

The JSON file is instructor validation metadata, not a file students need to type. Test-source filenames deliberately do not start with `test_`, so the full branch suite does not collect intermediate examples.
