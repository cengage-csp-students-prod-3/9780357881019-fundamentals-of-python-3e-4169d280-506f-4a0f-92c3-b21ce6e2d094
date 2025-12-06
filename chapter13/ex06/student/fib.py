"""
File: fib.py
Defines a memoized recursive Fibonacci function with a Counter.
"""

class Counter:
    """Counts recursive calls."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def fib(n):
    """Returns the nth Fibonacci number using memoization."""

    memo = {}
    counter = Counter()

    def helper(k):
        counter.increment()

        if k <= 1:
            return k

        value = memo.get(k)
        if value is not None:
            return value

        value = helper(k - 1) + helper(k - 2)
        memo[k] = value
        return value

    result = helper(n)
    return result   # <-- No printing!
