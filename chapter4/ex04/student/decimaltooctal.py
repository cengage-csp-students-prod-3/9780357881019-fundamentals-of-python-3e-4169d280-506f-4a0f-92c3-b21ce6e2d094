# decimaltooctal.py

def decimal_to_octal(decimal):
    if decimal == 0:
        return "0"

    octal_digits = []
    while decimal > 0:
        remainder = decimal % 8
        octal_digits.insert(0, str(remainder))  # prepend digit
        decimal = decimal // 8
    return ''.join(octal_digits)


def main():
    try:
        decimal_number = int(input("Enter a decimal integer: "))
        if decimal_number < 0:
            return  # Optional: silently ignore negatives
        octal = decimal_to_octal(decimal_number)
        print(octal)  # ✅ Print only the number — no extra text
    except ValueError:
        pass  # Optional: silently ignore bad input


if __name__ == "__main__":
    main()


# octaltodecimal.py

def octal_to_decimal(octal_str):
    decimal_value = 0
    power = 0

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
        print(decimal)  # ✅ Print only the result number
    except ValueError:
        pass  # Optional: silently ignore invalid input


if __name__ == "__main__":
    Nmain()
