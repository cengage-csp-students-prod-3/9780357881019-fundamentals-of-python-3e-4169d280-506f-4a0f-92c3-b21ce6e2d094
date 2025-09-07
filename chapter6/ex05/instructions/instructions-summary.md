## Instructions

Design, implement, and test a program in the file named **commandinterpreter.py** that uses a simple text-based command interpreter.

The program’s `main` function

<ol type="a">
    <li>Displays a menu of commands.</li>
    <li>Accepts an input command from the user.</li>
    <li>Calls a function to perform the command.</li>
    <li>Repeats steps _a_ through _c_ until the user selects the "Quit" command.</li>
</ol>

The program should define three other functions, named `printMenu`, `acceptCommand`, and `performCommand`, to carry out steps a, b, and c, respectively. The function to display the menu expects a list of menu options as an argument and displays these options prefixed with numbers. The function to accept an input command expects the length of the menu list as an argument. The function repeatedly prompts the user for a number in the range of options and takes inputs until the user enters a number within the range. The function either displays an error message for an invalid input or returns a valid input. The function to perform a command takes a command number and the menu as arguments and displays the selected command in the menu. Test your program with the menu ["Open", "Save", "Compile", "Run", "Quit"] and at least one other menu. Note that all menus must include a "Quit" command as the last item in the menu. (LO: 6.2)

An example of the program is shown below:

```txt
1 Open
2 Save
3 Compile
4 Run
5 Quit
Enter a number: 2
Command = Save
1 Open
2 Save
3 Compile
4 Run
5 Quit
Enter a number: 3
Command = Compile
1 Open
2 Save
3 Compile
4 Run
5 Quit
Enter a number: 5
Command = Quit
Have a nice day!
```

## Your Tasks
