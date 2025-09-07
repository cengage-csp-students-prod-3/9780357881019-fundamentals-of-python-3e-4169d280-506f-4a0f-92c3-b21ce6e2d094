## Instructions

Modify the guessing-game program of Section 3.5 in the file **guess.py** so that the user thinks of a number that the computer must guess. The computer must make no more than the minimum number of guesses, and it must prevent the user from cheating by entering misleading hints.

> _Hint_: Use the `math.log` function to compute the minimum number of guesses needed after the lower and upper bounds are entered. (LO: 3.3, 3.4)

Examples of the program are shown below:

```txt
Enter the smaller number: 0
Enter the larger number: 10

0 10
Your number is 5
Enter =, <, or >: <
0 4
Your number is 2
Enter =, <, or >: >
3 4
Your number is 3
Enter =, <, or >: =
Hooray, I've got it in 3 tries!
```

```txt
Enter the smaller number: 0
Enter the larger number: 50
0 50
Your number is 25
Enter =, <, or >: <
0 24
Your number is 12
Enter =, <, or >: <
0 11
Your number is 5
Enter =, <, or >: <
0 4
Your number is 2
Enter =, <, or >: <
0 1
Your number is 0
Enter =, <, or >: >
1 1
Your number is 1
Enter =, <, or >: >
I'm out of guesses, and you cheated!
```

## Your Tasks
