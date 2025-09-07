## Instructions

### Objective

Your goal is to create and thoroughly test a Python function named `myRange`. This function is to be defined in a file titled **testmyrange.py**. The purpose of `myRange` is to mimic the functionality of Python's built-in `range` function, but with a notable exception: instead of producing a range object, `myRange` will generate and return a list of integers. This exercise is designed to deepen your understanding of function parameters, control flow, and list operations in Python. **It is crucial that you do not use the built-in `range` function in your solution.**

### Function Requirements

1. **Parameters:**

   - The `myRange` function should accept three parameters. The first parameter represents the starting point of the range. The second and third parameters are optional; they represent the stopping point of the range and the step by which the range increments or decrements, respectively.
   - Utilize a default value of `None` for the second and third parameters to indicate that they are optional.

2. **Behavior:**

   - When the function is called with a single argument, treat this argument as the stopping point of the range, and set the starting point to `0`. The step, in this case, defaults to `1`.
   - When the function is called with two arguments, treat the first argument as the starting point and the second as the stopping point of the range. The step defaults to `1`.
   - When the function is called with all three arguments, the first argument is the starting point, the second is the stopping point, and the third is the step.
   - The function should produce a list of integers starting from the first argument up to, but not including, the second argument, incrementing by the third argument's value if the start is less than the stop. If the start is greater than the stop, the list should decrement.
   - If the step is `0` or leads to an infinite loop (e.g., step is positive when the start is greater than the stop or negative when the start is less than the stop), the function should return an empty list.

3. **Return Value:**
   - The function returns a list of integers calculated based on the arguments provided.

### Hints

- Begin by determining the actual values of the parameters based on the rules mentioned above. This involves handling cases where some parameters are not provided (i.e., are `None`).
- Next, use a loop to construct the list of integers. Pay careful attention to the direction in which you count (upward or downward) and ensure that your loop terminates correctly.
- Consider edge cases, such as when the step is `0` or does not logically align with the start and stop values, to prevent infinite loops.

### Learning Outcome (LO: 6.3)

Upon completing this task, you will have gained a deeper understanding of function definition, parameter handling, conditional statements, and loop constructs in Python. This exercise will also enhance your ability to translate complex requirements into working code.

### Testing Your Function

After defining the `myRange` function, you are expected to rigorously test its functionality to ensure it behaves as expected. Implement a `main` function within the **testmyrange.py** file that calls `myRange` with various combinations of arguments and prints the results. Examples of test calls include:

- `myRange(10)`
- `myRange(1, 10)`
- `myRange(1, 10, 2)`
- `myRange(10, 1, -1)`

Use these tests to verify that your function handles different scenarios correctly. Remember, thorough testing is key to ensuring the reliability of your implementation.

An example for the program is shown below:

```txt
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 3, 5, 7, 9]
```

## Your Tasks
