# Name: Mohan Dixit
# Date: Feb 14th
# Purpose: Turn mass and velocity into kinetic energy

m = float(input("Enter the mass of the object: "))
v = float(input("Enter the velocity of the object: "))

ke = (m*v**2)/2 # Calculate the kinetic energy

print(f"The kinetic energy is {ke}")