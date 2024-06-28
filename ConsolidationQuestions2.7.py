# Name: Mohan, Hassaan, and Hayder
# Date: March 8th
# Purpose: Check if someone's age matches


# Greeting message
print("This program checks to see if you qualify for the after-school program")

# Ask for their age

age = int(input("Enter your age: "))


#Check if they can join
if age <= 18 and age >= 12:
    print("You can join!")
else:
    print("You cant join!")
