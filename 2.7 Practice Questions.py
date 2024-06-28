# Name: Mohan, Hassaan, and Hayder
# Date: March 8th
# Purpose: Check if someone can sign up to library VIP


# Startings prints

print("Welcome to our library! To join our libraries VIP club, you need to meet these requirements: " +
      "\n Must have been a part of the library for at least 2 years"+
      "\n Must not have any overdue fines" +
      "\nMust be willing to accept all the terms and conditions\n")

# Get inputs

library_date = int(input("How long have you been a part of the library(years): "))
overdue_fines = int(input("How many overdue fines do you have? "))
terms_and_conditions = input("Do you accept the terms and conditions?(Yes or No) ")


# Check if they qual

if(library_date >= 2 and overdue_fines == 0 and terms_and_conditions == "Yes"):
    print("Congrars! You can join!")
else:
    print("Sorry, but you cannot join")
