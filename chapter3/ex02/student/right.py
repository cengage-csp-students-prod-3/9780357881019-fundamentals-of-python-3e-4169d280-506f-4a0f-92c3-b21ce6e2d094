# Write your program here
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))
square1 = side1 ** 2
square2 = side2 ** 2
square3 = side3 ** 2
if square1 + square2 == square3 or \
square2 + square3 == square1 or \
square1 + square3 == square2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
