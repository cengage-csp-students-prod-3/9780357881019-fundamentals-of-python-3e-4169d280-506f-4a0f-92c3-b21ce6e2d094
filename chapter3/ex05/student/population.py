# Write your program here
number = int(input("Enter the initial number of organisms: "))
rate = float(input("Enter the rate of growth [a real number > 1]: "))
cycleHours = int(input("Enter the number of hours to achieve the rate of growth: "))
totalHours = int(input("Enter the total hours of growth: "))

cycles = totalHours // cycleHours

for eachPass in range(cycles):
    number = number * rate

print("The total population is", int(number))