# Write your program here
def decimal_to_octal(decimal):
    if decimal == 0:
        return "0"
    
    octal_digits = []
    while decimal > 0:
        remainder = decimal % 8
        octal_digits.insert(0, str(remainder))
        decimal = decimal // 8
    return ''.join(octal_digits)


def main():
    try:
        decimal_input = int(input("Enter a decimal integer: "))
        if decimal_input < 0:
            print("Please enter a non-negative integer.")
            return
        octal_result = decimal_to_octal(decimal_input)
        print(f"The octal representation is {octal_result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == '__main__':
    main()
