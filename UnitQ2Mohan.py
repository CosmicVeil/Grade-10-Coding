# Name: Mohan Dixit
# Date: Feb 23rd
# Purpose: Perform different math operations on two numbers


# Get the two numbers
first_number = int(input("Enter an integer: "))
second_number = int(input("Enter another integer: "))


# Perform each operation and store it in a variable
summation = first_number+second_number
difference = first_number-second_number
product = first_number*second_number
quotient = float(first_number)/float(second_number)
exponent = float(first_number**second_number)


# Output the data
print(f"\nThe sum of these two numbers are: {summation}\nThe difference of these two numbers is: {difference}\n" +
      f"The product of these two numbers is: {product}\nThe quotient of these two numbers is: {quotient}\n"+
      f"{first_number} to the exponent {second_number} is {exponent}")

