"""Script a conversation instead of typing input during every test."""

from calculator.cli import run


def test_arithmetic_session(monkeypatch, capsys):
    answers = iter(["add", "10", "5", "subtract", "20", "7", "exit"])

    def scripted_input(prompt):
        return next(answers)

    monkeypatch.setattr("builtins.input", scripted_input)
    run()
    output = capsys.readouterr().out
    assert "Result: 15" in output
    assert "Result: 13" in output
    assert output.endswith("Goodbye!\n")


def test_invalid_input_then_recovery(monkeypatch, capsys):
    answers = iter(["pizza", "add", "hello", "help", "add", "2", "3", "exit"])

    def scripted_input(prompt):
        return next(answers)

    monkeypatch.setattr("builtins.input", scripted_input)
    run()
    output = capsys.readouterr().out
    assert "Unknown command." in output
    assert "Invalid number or result." in output
    assert "Commands:" in output
    assert "Result: 5" in output
