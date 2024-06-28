# Name: Mohan, Hassaan
# Date: March 4th
# Purpose: Show how much money goes into retirement plan


# Print out their retirement savings, and the money they have left after the 5% decrease
def print_savings(salary, bonus):
    print(f"The retirement savings from your salary is {salary*0.05}.\n The retirement savings from your bonus is {bonus*0.05}."
      + f"\nYour salary after the deduction is: {salary*0.95}, and your bonus after the deduction is: {bonus*0.95}")


    

# Greet the user
print("Hello! This program will take in your salary and your bonus, and return how much money goes into your retirement savings. ")


# Get the users salary and bonus
salary = float(input("Enter your salary: "))
bonus = float(input("Enter your bonus: "))


print_savings(salary, bonus)
