# Write your program here
import math
radius = float(input("Enter the sphere's radius: "))
diameter = 2 * radius
circumference = diameter * math.pi
surfaceArea = 4 * math.pi * radius * radius
volume = (4/3) * math.pi * radius ** 3
print("Diameter: ", diameter)
print("Circumference: ", circumference)
print("Surface area: ", surfaceArea)
print("Volume: ", volume)


