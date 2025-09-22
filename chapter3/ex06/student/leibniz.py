# Write your program here

iterations = int(input("Enter the number of iterations: "))
piApproximation = 0


for i in range(iterations):
    piApproximation += (-1) ** i / (2 * i + 1)

piApproximation *= 4

print("The approximation of pi is", piApproximation)
