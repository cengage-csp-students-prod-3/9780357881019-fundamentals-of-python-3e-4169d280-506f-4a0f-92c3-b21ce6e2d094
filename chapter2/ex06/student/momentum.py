# Write your program here
mass = float(input("Enter object's mass: "))
velocity = float(input("Enter the object's velocity: "))
momentum = mass * velocity
kineticEnergy = (1/2) * mass * velocity ** 2
print("The object's momentum is", str(momentum))
print("The object's kinetic energy is", str(kineticEnergy))