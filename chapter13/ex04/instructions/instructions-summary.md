## Instructions

An alternative strategy for the expo function uses the following recursive definition:

```python
expo(number, exponent)
    = 1, when exponent = 0
    = number * expo(number, exponent – 1), when exponent is odd
    = (expo(number, exponent // 2))2, when exponent is even
```

Define a recursive function `expo` (in the file **expo.py**) that uses this strategy and state its computational complexity using big-O notation. (LO: 13.2, 13.3)

<!--
{
    "CopyExercise": {
        "name": "expo.py",
        "copyTarget": "/chapter13/ex03/student/expo.py",
        "pasteTarget": "/expo.py"
    }
}
-->

## Your Tasks
