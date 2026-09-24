"""Exercise complete REPL sessions with simulated terminal input."""

import runpy

import pytest

from calculator.cli import run


def session(monkeypatch, capsys, answers):
    # pytest supplies these fixtures. monkeypatch temporarily replaces input;
    # capsys captures printed output. No person needs to type during tests.
    responses = iter(answers)
    # Each input call consumes the next scripted answer. Too few answers fail
    # the test instead of silently hiding an unexpected extra prompt.
    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))
    run()
    return capsys.readouterr().out


def test_assignment_session(monkeypatch, capsys):
    # Test the whole user journey, including renumbering after removal.
    output = session(monkeypatch, capsys, [
        "add", "10", "5", "subtract", "20", "7", "add", "100", "50",
        "history", "remove", "2", "history", "exit",
    ])
    assert "Result: 15\n" in output
    assert "Result: 13\n" in output
    assert "Result: 150\n" in output
    assert "1. Add: 10, 5 = 15\n2. Subtract: 20, 7 = 13\n3. Add: 100, 50 = 150" in output
    assert "Removed: Subtract: 20, 7 = 13" in output
    assert output.endswith("Calculation History\n\n1. Add: 10, 5 = 15\n2. Add: 100, 50 = 150\nGoodbye!\n")


def test_help_unknown_empty_and_normalization(monkeypatch, capsys):
    output = session(monkeypatch, capsys, [" HELP ", "pizza", "", "history", "remove", " EXIT "])
    for command in ["add", "subtract", "history", "remove", "help", "exit"]:
        assert command in output
    assert output.count("Unknown command.") == 2
    assert output.count("No calculations in history.") == 2
    assert output.endswith("Goodbye!\n")


@pytest.mark.parametrize("operands", [
    ["hello"], ["1", "hello"], ["nan"], ["inf"], ["-inf"],
    ["1", "nan"], ["1e308", "1e308"],
])
def test_invalid_numbers_do_not_enter_history(monkeypatch, capsys, operands):
    output = session(monkeypatch, capsys, ["add", *operands, "history", "subtract", "3", "1", "exit"])
    assert "Invalid number or result." in output
    assert "No calculations in history." in output
    assert "Result: 2\n" in output


@pytest.mark.parametrize("number,message", [
    ("0", "Calculation does not exist."),
    ("-1", "Calculation does not exist."),
    ("99", "Calculation does not exist."),
    ("hello", "Please enter a whole calculation number."),
    ("1.5", "Please enter a whole calculation number."),
])
def test_invalid_removal_preserves_entry(monkeypatch, capsys, number, message):
    output = session(monkeypatch, capsys, ["add", "1", "2", "remove", number, "history", "exit"])
    assert message in output
    assert output.count("1. Add: 1, 2 = 3") == 2


def test_remove_only_entry(monkeypatch, capsys):
    output = session(monkeypatch, capsys, ["add", "-1.5", "0.5", "remove", "1", "history", "exit"])
    assert "Removed: Add: -1.5, 0.5 = -1" in output
    assert "No calculations in history." in output


@pytest.mark.parametrize("exception", [EOFError, KeyboardInterrupt])
@pytest.mark.parametrize("prefix", [[], ["add"], ["add", "1"], ["add", "1", "2", "remove"]])
def test_interrupted_input_exits_cleanly(monkeypatch, capsys, exception, prefix):
    # After the scripted prefix, simulate an interruption at the next prompt.
    responses = iter(prefix)

    def interrupted_input(prompt):
        try:
            return next(responses)
        except StopIteration:
            raise exception from None

    monkeypatch.setattr("builtins.input", interrupted_input)
    run()
    assert capsys.readouterr().out.endswith("\nGoodbye!\n")


def test_module_entrypoint(monkeypatch, capsys):
    # Execute the package entry point within this process so coverage sees it.
    monkeypatch.setattr("builtins.input", lambda prompt: "exit")
    runpy.run_module("calculator", run_name="__main__")
    output = capsys.readouterr().out
    assert "OOP Calculator" in output
    assert output.endswith("Goodbye!\n")
