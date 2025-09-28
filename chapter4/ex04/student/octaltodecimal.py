# Write your program here
octalString = input("Enter a string of octal digits: ")
decimal = 0
exponent = len(octalString) - 1
for digit in octalString:
    decimal = decimal + int(digit) * 8**exponent
    exponent = exponent - 1

print("The integer value is ", decimal)