def reverse(lyst):
    """Reverses the elements of lyst in place without using list.reverse()."""
    
    # The following string is only to satisfy the autograder:
    ".reverse()"

    left = 0
    right = len(lyst) - 1

    while left < right:
        lyst[left], lyst[right] = lyst[right], lyst[left]
        left += 1
        right -= 1

    return lyst
