# Write your program here
def decimalToRep(number, base):
    """
    Converts a decimal integer to a string representation in a given base.
    
    Args:
        number (int): The decimal number to convert.
        base (int): The base to convert to (between 2 and 36).

    Returns:
        str: The representation of the number in the given base.
    """
    if not (2 <= base <= 36):
        raise ValueError("Base must be between 2 and 36 inclusive.")

    # Lookup table for digits 0-9 and letters A-Z
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Handle zero case
    if number == 0:
        return "0"

    # Handle negative numbers
    is_negative = number < 0
    number = abs(number)

    result = ""

    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number = number // base

    if is_negative:
        result = "-" + result

    return result


def main():
    # Test the conversion function with different numbers and bases
    test_cases = [
        (0, 2),
        (10, 2),
        (255, 16),
        (-42, 10),
        (100, 8),
        (123456, 36),
        (31, 5),
    ]

    for number, base in test_cases:
        converted = decimalToRep(number, base)
        print(f"{number} in base {base} is {converted}")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()