"""
File: fib.py
Memoized Fibonacci that counts only new computations.
"""

class Counter:
    """Counts Fibonacci computations."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def fib(n, counter):
    """Returns Fibonacci(n) using memoization and counts only NEW computations."""

    memo = {}

    def helper(k):
        # If value already computed, do NOT increment
        if k in memo:
            return memo[k]

        # We are computing a NEW Fibonacci number → count it
        counter.increment()

        # Base cases (textbook convention)
        if k == 0 or k == 1:
            memo[k] = 1
        else:
            memo[k] = helper(k - 1) + helper(k - 2)

        return memo[k]

    return helper(n)
