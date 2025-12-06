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

    memo = {}            # dictionary for memoized values
    counter = Counter()  # count recursive calls

    def helper(k):
        counter.increment()

        # Base cases
        if k <= 1:
            return k

        # Check memo
        value = memo.get(k)
        if value is not None:
            return value

        # Recursive computation
        value = helper(k - 1) + helper(k - 2)

        # Store in memo
        memo[k] = value
        return value

    result = helper(n)

    # Print number of recursive calls (as required by directions)
    print(counter.count)

    return result
