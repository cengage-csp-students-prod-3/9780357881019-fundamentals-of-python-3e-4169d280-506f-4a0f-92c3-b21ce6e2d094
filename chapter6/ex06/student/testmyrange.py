# Write your code here
def myRange(start, stop=None, step=None):
    """
    A custom implementation of Python's built-in range function,
    returning a list of integers instead of a range object.
    """

    # Handle arguments according to how range() works
    if stop is None:
        # Called with one argument: myRange(stop)
        stop = start
        start = 0

    if step is None:
        step = 1

    # If step is 0, return empty list (avoid infinite loop)
    if step == 0:
        return []

    result = []

    # Increasing range
    if step > 0:
        current = start
        while current < stop:
            result.append(current)
            current += step

    # Decreasing range
    elif step < 0:
        current = start
        while current > stop:
            result.append(current)
            current += step

    return result


def main():
    # Test 1: Single argument (stop only)
    print(myRange(10))          # Expected: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test 2: Two arguments (start, stop)
    print(myRange(1, 10))       # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test 3: Three arguments (start, stop, step)
    print(myRange(1, 10, 2))    # Expected: [1, 3, 5, 7, 9]

    # Test 4: Decreasing range
    print(myRange(10, 1, -1))   # Expected: [10, 9, 8, 7, 6, 5, 4, 3, 2]

    # Test 5: Step = 0 (invalid)
    print(myRange(1, 10, 0))    # Expected: []

    # Test 6: Step direction mismatch (positive step but start > stop)
    print(myRange(10, 1, 2))    # Expected: []

    # Test 7: Step direction mismatch (negative step but start < stop)
    print(myRange(1, 10, -2))   # Expected: []

    # Test 8: Edge case – start == stop
    print(myRange(5, 5))        # Expected: []


# Run tests when executed directly
if __name__ == "__main__":
    main()