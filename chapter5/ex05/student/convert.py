# Write your program here
digit_table = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def repToDecimal(value_str, base):
    """
    Converts a string representation of a number in the given base to decimal.
    
    Parameters:
        value_str (str): The string representation of the number.
        base (int): The base of the number system (e.g., 2, 8, 16).
    
    Returns:
        int: The decimal (base-10) equivalent of the input number.
    """
    value_str = value_str.upper()  # Ensure all letters are uppercase
    decimal_value = 0
    power = 0
    
    for digit_char in reversed(value_str):
        if digit_char not in digit_table or digit_table[digit_char] >= base:
            raise ValueError(f"Invalid digit '{digit_char}' for base {base}")
        
        digit_value = digit_table[digit_char]
        decimal_value += digit_value * (base ** power)
        power += 1
    
    return decimal_value


def main():
    # Test cases
    print(repToDecimal("10", 2))     # 2
    print(repToDecimal("10", 8))     # 8
    print(repToDecimal("10", 10))    # 10
    print(repToDecimal("10", 16))    # 16
    print(repToDecimal("1A", 16))    # 26
    print(repToDecimal("FF", 16))    # 255
    print(repToDecimal("777", 8))    # 511
    print(repToDecimal("1010", 2))   # 10

if __name__ == "__main__":
    main()