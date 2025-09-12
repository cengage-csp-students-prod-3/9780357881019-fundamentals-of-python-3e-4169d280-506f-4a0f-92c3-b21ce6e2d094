# Write your program here
newVideos = float(input("Enter the number of new videos: "))
oldies = float(input("Enter the number of oldies: "))
totalCost = newVideos * 3 + oldies * 2
print("The total cost is $" + str(round(totalCost)))