# octaltodecimal.py

def octal_to_decimal(octal_str):
    decimal_value = 0
    power = 0

    # Go through each digit from right to left
    for digit in reversed(octal_str):
        if digit not in '01234567':
            raise ValueError("Invalid octal digit found.")
        decimal_value += int(digit) * (8 ** power)
        power += 1
    return decimal_value


def main():
    octal_input = input("Enter a string of octal digits: ").strip()

    try:
        decimal_result = octal_to_decimal(octal_input)
        print(f"The integer value is {decimal_result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
