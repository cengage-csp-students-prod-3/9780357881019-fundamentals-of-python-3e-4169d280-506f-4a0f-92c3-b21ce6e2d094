# Write your code here
import math

TOLERANCE = 0.000001

def newton(x):

    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= TOLERANCE:
            break

    return estimate

def main():
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
            break

        x = float(x)
