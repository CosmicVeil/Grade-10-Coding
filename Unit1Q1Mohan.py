# Name: Mohan Dixit
# Date: Feb 23rd
# Purpose: Calculate revenue for a drama production based on students and parents


# Get the input and the cost of the student and parent seating
cost_of_student_seats = float(input("Enter cost for student seats: "))
cost_of_parent_seats = float(input("Enter cost for parent seats: "))

# Get the number of students and parents

number_of_students = int(input("The number of students = "))
number_of_parents = int(input("The number of parents = "))

# Calculate the profit

profit_from_sales = cost_of_student_seats*number_of_students + cost_of_parent_seats*number_of_parents

# Print out the profit

print("\nThe profit of the sales if full house is: $" + str(profit_from_sales))
