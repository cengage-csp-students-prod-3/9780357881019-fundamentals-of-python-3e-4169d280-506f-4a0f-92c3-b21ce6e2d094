# Write your code here

def reverse(lyst):
    """Reverses the elements of lyst in place without using list.reverse()."""
    left = 0
    right = len(lyst) - 1

    # Swap mirror elements until the middle is reached
    while left < right:
        lyst[left], lyst[right] = lyst[right], lyst[left]
        left += 1
        right -= 1
