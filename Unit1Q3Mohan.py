# Name: Mohan Dixit
# Date: Feb 23rd
# Purpose: Ask a user for their name, age, how much they make and current year.
# Then, print out a greeting and how much they will have in 10,20,30 years


# Get all the information from the user

name = input("What is your name? ")
age = int(input("How old are you? "))
money_per_month = int(input("How much money do you save per month? "))
current_year = int(input("What is the current year? "))


# Find out the money they earn 10 years from now, 20 years from now, and 30 years from now
money_in_10years = 120*money_per_month
money_in_20years = 240*money_per_month
money_in_30years = 360*money_per_month


# Print out a greeting

print(f"\nHello {name}! You are {age} years old in {current_year}!")

# Print out their earnings

print(f"In 10 years, you will have ${money_in_10years}. In 20 years, you will have ${money_in_20years}. In 30 years, you will have ${money_in_30years}.")
