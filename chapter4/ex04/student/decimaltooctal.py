# octal_converter.py

def decimal_to_octal(decimal):
    if decimal == 0:
        return "0"

    octal_digits = []
    while decimal > 0:
        remainder = decimal % 8
        octal_digits.insert(0, str(remainder))
        decimal = decimal // 8
    return ''.join(octal_digits)


def octal_to_decimal(octal_str):
    decimal_value = 0
    power = 0

    for digit in reversed(octal_str):
        if digit not in '01234567':
            raise ValueError("Invalid octal digit.")
        decimal_value += int(digit) * (8 ** power)
        power += 1

    return decimal_value


def main():
    print("Choose conversion type:")
    print("1. Decimal to Octal")
    print("2. Octal to Decimal")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        try:
            decimal_input = int(input("Enter a decimal integer: "))
            if decimal_input < 0:
                return
            octal_result = decimal_to_octal(decimal_input)
            print(octal_result)  # ✅ Output must be clean
        except ValueError:
            return

    elif choice == "2":
        octal_input = input("Enter a string of octal digits: ").strip()
        try:
            decimal_result = octal_to_decimal(octal_input)
            print(decimal_result)  # ✅ Output must be clean
        except ValueError:
            return

    else:
        return  # Invalid option; exit silently


if __name__ == "__main__":
    main()
