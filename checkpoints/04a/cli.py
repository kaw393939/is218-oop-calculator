"""Checkpoint 4A: a small conversation before adding history commands."""

from calculator.calculation import Add, Subtract


HELP = "Commands: add, subtract, help, exit"


def run():
    operations = {"add": Add, "subtract": Subtract}
    print('OOP Calculator\n\nType "help" for commands.')
    while True:
        command = input("> ").strip().lower()
        if command == "exit":
            break
        if command in operations:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            operation_class = operations[command]
            calculation = operation_class(a, b)
            print(f"Result: {calculation.get_result():g}")
        elif command == "help":
            print(HELP)
        else:
            print('Unknown command.\nType "help" for available commands.')
    print("Goodbye!")
