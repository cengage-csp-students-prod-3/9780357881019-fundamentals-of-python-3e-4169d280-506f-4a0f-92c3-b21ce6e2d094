# Write your code here

"""
File: fib.py
Defines a memoized recursive Fibonacci function with a Counter.
"""

class Counter:
    """Simple counter class."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def __str__(self):
        return str(self.count)


def fibonacci(n):
    """Returns the nth Fibonacci number using memoization."""

    memo = {}                 # dictionary for memoized values
    counter = Counter()       # counts recursive calls

    def helper(k):
        counter.increment()

        # Base cases
        if k <= 1:
            return k

        # Check memo dictionary
        value = memo.get(k, None)
        if value is not None:
            return value

        # Recursive computation
        value = helper(k - 1) + helper(k - 2)

        # Save in memo
        memo[k] = value
        return value

    result = helper(n)

    print("Number of recursive calls:", counter)

    return result
