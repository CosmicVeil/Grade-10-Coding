# Name: Mohan Dixit
# Date: March 20th
# Purpose: Check to see if some dates are special

# Get today's day
day = input("Enter today's date in the format DD/MM/YY: ")


# Split the string into a list, so we can access each individual element(Day, Month, Year)
list_day = list(map(int,day.split("/")))

# Check if it is magic

if list_day[0]*list_day[1] == list_day[2]:
    print("Congrats!", day, "is a magic day!")
else:
    print("Oh No!", day, "is not a magic day")

