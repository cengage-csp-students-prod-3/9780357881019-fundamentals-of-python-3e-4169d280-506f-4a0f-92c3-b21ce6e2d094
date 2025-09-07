## Instructions

Suppose that Python does not include the higher-order functions map, filter, and reduce. Define three corresponding functions, named `myMap`, `myFilter`, and `myReduce`, in a new module named `hof` (in the file **hof.py**). The `myMap` and `myFilter` functions expect a function of one argument and a list as arguments and return a list of the results. The `myReduce` function expects a function of two arguments and a nonempty list as arguments and returns a single value. Test your functions in a short tester program (in the file **testhof.py**) that compares their behavior to that of Python’s own map, filter, and reduce functions. (LO: 7.2)

An example of the program is shown is below:

```
Argument list:   [0, 1, 2, 3, 4]
map with ** 2  : [0, 1, 4, 9, 16]
myMap with ** 2: [0, 1, 4, 9, 16]
filter with odd  : [1, 3]
myFilter with odd: [1, 3]
reduce with +   : 10
myReduce with + : 10
Argument list:   [3]
reduce with +   : 3
myReduce with + : 3
Argument list:   []
map with ** 2  : []
myMap with ** 2: []
filter with odd  : []
myFilter with odd: []
```

## Your Tasks
