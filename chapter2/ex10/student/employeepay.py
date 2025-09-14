# Write your program here
wage = float(input("Enter the wage: "))
regHours = float(input("Enter the regular hours: "))
overHours = float(input("Enter the overtime hours: "))
overTime = overHours * wage * 1.5
totalWeeklyPay = wage * regHours + overTime
print("The total weekly pay is $" + str(round(totalWeeklyPay, 2)))