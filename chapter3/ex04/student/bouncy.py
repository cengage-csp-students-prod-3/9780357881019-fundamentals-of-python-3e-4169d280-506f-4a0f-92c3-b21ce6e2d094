# Write your program here
height = float(input("Enter the height from which the is dropped: "))
bounciness = float(input("Enter the bounciness index of thr ball: "))
bounces = int(input("Enter then number of times the ball is allowed to continue bouncing: "))
distance = 0

for eachPass in range(bounces):
    distance += height
    bounceHeight = height * bounciness
    height = bounceHeight
    distance += bounceHeight

print("The total disrance traveled is:", distance, "units.")