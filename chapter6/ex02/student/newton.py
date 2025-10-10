# Write your code here
import math

TOLERANCE = 0.000001

def newton(x):

    estimate = 1.0
    while True:
        estimate = improveEstimate(x, estimate)
        
        if limitReached(x, estimate):
            break

    return estimate

def limitReached(x, estimate):
    difference = abs(x - estimate ** 2)
    return difference <= TOLERANCE

def improveEstimate(x, estimate):
    return (estimate + x / estimate) 

def main():
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
            break

        x = float(x)
        print("The program's estimate is ", newton(x))
        print("Python's estimate is      ", math.sqrt(x))

if __name__ == "__main__":
    main()