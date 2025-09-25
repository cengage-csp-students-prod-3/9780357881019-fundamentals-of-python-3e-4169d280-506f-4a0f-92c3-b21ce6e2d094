# decimaltooctal.py
# Converts a decimal integer to an octal string using manual algorithm

def decimal_to_octal(decimal):
    if decimal == 0:
        return "0"

    octal_digits = []
    while decimal > 0:
        remainder = decimal % 8
        octal_digits.insert(0, str(remainder))  # prepend the digit
        decimal = decimal // 8
    return ''.join(octal_digits)


def main():
    try:
        decimal_number = int(input("Enter a decimal integer: "))
        if decimal_number < 0:
            print("Please enter a non-negative integer.")
            return

        octal = decimal_to_octal(decimal_number)
        print(f"The octal representation is {octal}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()

# octaltodecimal.py
# Converts an octal string to a decimal integer using manual algorithm

def octal_to_decimal(octal_str):
    decimal_value = 0
    power = 0

    # Reverse the string to process from right to left
    for digit in reversed(octal_str):
        if digit not in '01234567':
            raise ValueError("Invalid octal digit.")
        decimal_value += int(digit) * (8 ** power)
        power += 1

    return decimal_value


def Nmain():
    octal_input = input("Enter a string of octal digits: ").strip()

    try:
        decimal = octal_to_decimal(octal_input)
        print(f"The integer value is {decimal}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    Nmain()
