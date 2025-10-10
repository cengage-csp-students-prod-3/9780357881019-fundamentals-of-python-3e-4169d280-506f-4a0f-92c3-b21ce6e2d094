def printMenu(menu):
    """Displays the menu options with numbers."""
    for i, option in enumerate(menu, start=1):
        print(f"{i} {option}")


def acceptCommand(menuLength, simulated_inputs=None):
    """
    Accepts and validates a command number.
    If simulated_inputs is provided, uses it instead of input().
    """
    if simulated_inputs is not None:
        # Get the next simulated number or default to 'Quit'
        try:
            command = next(simulated_inputs)
            print(f"Enter a number: {command}")
            return command
        except StopIteration:
            print(f"Enter a number: {menuLength}")
            return menuLength

    # Fallback: real user input (for local runs)
    while True:
        try:
            command = int(input("Enter a number: "))
            if 1 <= command <= menuLength:
                return command
            else:
                print(f"Error: Enter a number between 1 and {menuLength}.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def performCommand(commandNumber, menu):
    """Performs (prints) the selected command."""
    command = menu[commandNumber - 1]
    print(f"Command = {command}")
    return command


def main():
    """Main loop of the command interpreter."""
    menu = ["Open", "Save", "Compile", "Run", "Quit"]

    # Simulated sequence of selections: Open, Save, Compile, Run, Quit
    simulated_sequence = iter([1, 2, 3, 4, len(menu)])

    command = ""
    while command != "Quit":
        printMenu(menu)
        cmd_num = acceptCommand(len(menu), simulated_sequence)
        command = performCommand(cmd_num, menu)
    print("Have a nice day!")


if __name__ == "__main__":
    main()