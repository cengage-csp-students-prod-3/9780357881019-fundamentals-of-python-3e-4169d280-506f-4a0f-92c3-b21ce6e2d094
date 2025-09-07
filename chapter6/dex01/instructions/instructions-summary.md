## Instructions

Jack is developing a function named `shuffleString`, which rearranges the characters is a given string in random positions. He reasons that he can split the string into a list of its characters, then shuffle this list, and finally join the resulting list back into a string. He tries out his strategy for this task in the Python shell, as follows:

```python
import random
def shuffleString(theString):
    print("".join(random.shuffle(list(theString))))
shuffleString("Apples are red")
```

```txt
Traceback (most recent call last):
    File "<shuffle.py>", line 1, in <module>
        shuffleString("Apples are red")
    File "<shuffle.py>", line 2, in shuffleString
        print("".join(random.shuffle(list(theString))))
TypeError: can only join an iterable
```

Jack’s strategy does not appear to produce the expected result. Determine the cause of the error and correct it.

## Your Tasks
