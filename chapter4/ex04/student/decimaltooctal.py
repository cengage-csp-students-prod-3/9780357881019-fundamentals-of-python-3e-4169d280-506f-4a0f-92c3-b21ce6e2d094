decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    octalString = ""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        octalString = str(remainder) + octalString

    print("The octal representation is", octalString)

