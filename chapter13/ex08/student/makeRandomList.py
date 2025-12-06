import random

def makeRandomList(size):
    """Creates and returns a list of unique random numbers
    from 1 to size in random order."""
    lyst = []
    for count in range(size):
        while True:
            number = random.randint(1, size)   # O(1)
            if not number in lyst:            # O(k) list membership test
                lyst.append(number)           # O(1)
                break
    return lyst
