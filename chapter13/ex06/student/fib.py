class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def fib(n):
    memo = {}
    counter = Counter()

    def helper(k):
        counter.increment()

        # Base cases (textbook version)
        if k == 0 or k == 1:
            return 1

        # Check memo
        value = memo.get(k)
        if value is not None:
            return value

        value = helper(k - 1) + helper(k - 2)
        memo[k] = value
        return value

    return helper(n)
