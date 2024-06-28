
# Name: Mohan Dixit
# Date: Feb 12th
# Purpose: We ask the user for the number of courses they have. Take their course name and average for the course, and finally print out their average and highest mark. 


num_of_subject = int(input("Input the number of subjects you have this semester: "))

max_mark = 0
max_subject = None
average_mark = 0

for i in range(0,num_of_subject):
    subject = input(f"What is your {i+1} subject? ")
    average = float(input(f"What is your average in {subject}? "))

    if average > max_mark:
        max_mark = average
        max_subject = subject
        
    average_mark += average

average_mark = average_mark/num_of_subject

print(f"Your average for this semester was {average_mark}. The highest mark you had was {max_mark}%, in {max_subject}")
    
