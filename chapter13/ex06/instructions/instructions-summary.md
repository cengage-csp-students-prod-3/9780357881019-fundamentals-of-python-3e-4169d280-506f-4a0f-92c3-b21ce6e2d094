## Instructions

Modify the recursive Fibonacci function (in the file **fib.py**) to employ the memoization technique discussed in this chapter. The function creates a dictionary and then defines a nested recursive helper function. The base case is the same as before. However, before making a recursive call, the helper function looks up the value for the function’s current argument in the dictionary (use the method `get`, with `None` as the default value). If the value exists, the function returns it. Otherwise, after the helper function adds the results of its two recursive calls, it saves the sum in the dictionary with the current argument of the function as the key. Also use the `Counter` object discussed in this chapter to count the number of recursive calls of the helper function. (LO: 13.2, 13.6)

## Your Tasks
