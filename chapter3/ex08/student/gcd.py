# Write your program here
smallerNum = int(input("Enter the smaller number: "))
largerNum = int(input("Enter the larger number: "))

if smallerNum > largerNum:
    smallerNum, largerNum = largerNum, smallerNum

while smallerNum != 0:
    remainder = largerNum % smallerNum
    largerNum, smallerNum = smallerNum, remainder

print("The greatest common divisor is", largerNum)