# Name: Mohan
# Purpose: Seating Arrangement


rows = int(input("How many rows of tables are in your class? "))
columns = int(input("How many columns of tables are in your class? "))

tables = [[]]

# Initialize the arrangment

for i in range(rows):
    for j in range(columns):
        tables[i].append("Empty")
    tables.append([])



students = int(input("How many students are in your class? "))

# Loop through where each students wants to sit

for i in range(students):

    # Get their name and preferred seat

    name = input(f"What is one student's name? ")
    pref_row = int(input("What is the student's preferred row? "))
    pref_column = int(input("What is the student's preferred column? "))

    # Check to see if the input they enter is valid, and also to check if the seat is taken

    while pref_row > rows or pref_column > columns or tables[pref_row-1][pref_column-1] != "Empty":
        
        # Checks if their preferred row or column was over the number of rows and columns in their class
        if  pref_row > rows or pref_column > columns:
            print("The row or column number are over the number of rows and colums in the class!")
            print("Choose another seat!")

        # Checks if the seat is taken
        else:
            print("That seat is taken! Choose another")

        # Asks them to reenter
        pref_row = int(input("What is the student's preferred row? "))
        pref_column = int(input("What is the student's preferred column? "))

    
    # When a correct value is entered, we save it to the seating chart
    tables[pref_row-1][pref_column-1] = name


# We print it out

print("\nHere is the desired seating chart: \n\n")

for i in range(rows):
    for j in range(columns):
        print(tables[i][j], "\t", end='')
    print()
