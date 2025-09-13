# Write your program here
years = float(input("Enter the number of years: "))
rate = 3 * 10 ** 8
seconds = 365 * 24 * 60 * 60
distance = rate * seconds * years
print("Light travels", int(distance), "meters in", int(years), "years.")