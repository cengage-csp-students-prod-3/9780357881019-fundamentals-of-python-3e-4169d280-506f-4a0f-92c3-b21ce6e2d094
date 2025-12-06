# Write your code here

def expo(number, exponent):
    """Returns number raised to the given nonnegative exponent using
    recursive exponentiation by squaring."""
    
    # Base case
    if exponent == 0:
        return 1
    
    # If exponent is odd
    if exponent % 2 == 1:
        return number * expo(number, exponent - 1)
    
    # If exponent is even
    half = expo(number, exponent // 2)
    return half * half
