"""A first REPL: calculate now, connect history in the next stage."""

from math import isfinite

from calculator.calculation import Add, Subtract


HELP = "Commands: add, subtract, help, exit"


def read_number(prompt: str) -> float:
    """Convert input text and reject values such as infinity or NaN."""
    number = float(input(prompt))
    if not isfinite(number):
        raise ValueError("A finite number is required.")
    return number


def run() -> None:
    """Read, evaluate, print, and repeat."""
    # Values in this dictionary are classes; calling one creates an object.
    operations = {"add": Add, "subtract": Subtract}
    print('OOP Calculator\n\nType "help" for commands.')
    while True:
        try:
            command = input("> ").strip().lower()
            if command == "exit":
                break
            if command == "help":
                print(HELP)
                continue
            if command not in operations:
                print('Unknown command.\nType "help" for available commands.')
                continue
            try:
                a = read_number("First number: ")
                b = read_number("Second number: ")
                operation_class = operations[command]
                calculation = operation_class(a, b)
                result = calculation.get_result()
                if not isfinite(result):
                    raise ValueError("Result is outside the supported range.")
            except ValueError:
                print("Invalid number or result. Please use finite numbers.")
                continue
            print(f"Result: {result:g}")
        except (EOFError, KeyboardInterrupt):
            # This handler also covers interruption during either operand prompt.
            print()
            break
    print("Goodbye!")
