# Write your program here
startSalary = float(input("Enter the starting salary: $"))
increase = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))

print("\nYear   Salary")
print("-------------")

salary = startSalary

for year in range(1, years + 1):
    print(f"{year:2}    {salary:.2f}")
    salary *= (1 + increase / 100)