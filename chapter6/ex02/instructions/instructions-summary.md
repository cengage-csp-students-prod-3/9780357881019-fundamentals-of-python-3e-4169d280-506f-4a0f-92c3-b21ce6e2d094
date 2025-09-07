## Instructions

Restructure Newton’s method (_Case Study 3-2_) by decomposing it into three cooperating functions (including the original `newton` method.). The task of testing for the limit is assigned to a function named `limitReached`, whereas the task of computing a new approximation is assigned to a function named `improveEstimate`. Each function, in the file named **newton.py**, expects the relevant arguments and returns an appropriate value. (LO: 6.2)

Required methods to implement for this exercise:

```
    newton(x): Returns the square root of x
    improveEstimate(x, estimate): Returns the new estimate by using the formula (estimate + x / estimate) / 2
    limitReached(x, estimate): Returns True if the differences is less than or equal to the global TOLERANCE variable, else False
```

An example of the program is shown below:

```txt
Enter a positive number or enter/return to quit: 2
The program's estimate is 1.4142135623746899
Python's estimate is      1.4142135623730951
Enter a positive number or enter/return to quit: 4
The program's estimate is 2.0000000929222947
Python's estimate is      2.0
Enter a positive number or enter/return to quit: 9
The program's estimate is 3.000000001396984
Python's estimate is      3.0
Enter a positive number or enter/return to quit:
```

<!--
{
    "CopyExercise": {
        "name": "newton.py",
        "copyTarget": "/chapter6/ex01/student/newton.py",
        "pasteTarget": "/newton.py"
    }
}
-->

## Your Tasks
