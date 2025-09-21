# Write your program here
# TKTK: Add started code here.
import math
smallNum = int(input("Enter the smaller number: "))
bigNum = int(input("Enter the larger number: "))
maxGuesses = round(math.log(bigNum - smallNum + 1, 2))
count = 0;

while True:
    count += 1
    print(smallNum, bigNum)
    yourNum = (smallNum + bigNum) // 2
    print("Your number is", yourNum)
    answer = input("Enter =, <, or >: ")

    if answer == "=":
        print("Hooray, I've got it in", count, "tries!")
        break
    elif count == maxGuesses:
        print("I'm out of guesses, and you cheated!")
        break
    elif answer == "<":
        bigNum = yourNum - 1
    else:
        smallNum = yourNum + 1
