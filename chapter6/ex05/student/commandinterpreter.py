# Write your code here
def printMenu(menu):
    """
    Displays the menu options with numbers.
    :param menu: List of menu items
    """
    for i, option in enumerate(menu, start=1):
        print(f"{i} {option}")


def acceptCommand(menuLength):
    """
    Prompts the user to enter a valid command number.
    :param menuLength: The number of items in the menu
    :return: The valid command number (int)
    """
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
    """
    Performs (prints) the selected command.
    :param commandNumber: The number selected by the user
    :param menu: The list of menu items
    """
    command = menu[commandNumber - 1]
    print(f"Command = {command}")
    return command


def main():
    """
    Main function that drives the command interpreter.
    Displays the menu, accepts user input, performs commands,
    and repeats until the user selects "Quit".
    """
    # Test menus
    menus_to_test = [
        ["Open", "Save", "Compile", "Run", "Quit"],
        ["Add Record", "Delete Record", "Search Record", "Quit"]
    ]

    # Run the interpreter for each test menu
    for menu in menus_to_test:
        print("\n--- New Menu Test ---")
        command = ""
        while command != "Quit":
            printMenu(menu)
            cmd_num = acceptCommand(len(menu))
            command = performCommand(cmd_num, menu)
        print("Have a nice day!")


# Only run main if this file is executed directly
if __name__ == "__main__":
    main()