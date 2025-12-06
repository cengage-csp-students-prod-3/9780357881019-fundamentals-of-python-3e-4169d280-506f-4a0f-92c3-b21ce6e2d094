# Write your code here

def expo(number, exponent):
    """Returns number raised to the given nonnegative exponent."""
    result = 1
    for _ in range(exponent):
        result *= number
    return result
