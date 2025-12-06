"""
File: fib.py
Memoized Fibonacci function that accepts a Counter object and
counts recursive calls.
"""

class Counter:
    """Simple counter to track recursive calls."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def fib(n, counter):
    """
    Returns the nth Fibonacci number using memoization.
    Accepts a Counter object to count recursive calls.
    """

    memo = {}        # memoization dictionary

    def helper(k):
        counter.increment()   # count every recursive call

        # Base cases (this textbook uses fib(0)=1, fib(1)=1)
        if k == 0 or k == 1:
            return 1

        # Check memo
        value = memo.get(k)
        if value is not None:
            return value

        # Compute and store result
        value = helper(k - 1) + helper(k - 2)
        memo[k] = value
        return value

    return helper(n)
