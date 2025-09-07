<!-- manual -->

## Instructions

The function `makeRandomList` creates and returns a list of numbers of a given size (its argument). The numbers in the list are unique and range from 1 through the size. They are placed in random order. Here is the code for the function:

```python
def makeRandomList(size):
    lyst = []
    for count in range(size):
        while True:
            number = random.randint(1, size)
            if not number in lyst:
                lyst.append(number)
                break
    return lyst
```

You may assume that `range`, `randint`, and append are constant time functions. You may also assume that `random.randint` more rarely returns duplicate numbers as the range between its arguments increases. State the computational complexity of this function using big-O notation and justify your answer. (LO: 13.2, 13.6)

## Your Tasks
