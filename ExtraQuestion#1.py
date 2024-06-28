# Name: Mohan
# Purpose: Seating Arrangement


rows = int(input("How many rows of tables are in your class? "))
columns = int(input("How many columns of tables are in your class? "))

tables = [["Empty"]*columns]*rows

students = int(input("How many students are in your class? "))

for i in range(students):

    name = input(f"What is the {i+1} student's name? ")
    pref_row = int(input("What is the student's preferred row? "))
    pref_column = int(input("What is the student's preferred column? "))

    while pref_row > rows or pref_column > columns or tables[pref_row-1][pref_column-1] != "Empty":
        
        if  pref_row > rows or pref_column > columns:
            print("The row or column number are over the number of rows and colums in the class!")
        else:
            print("That seat is taken! Choose another")
        pref_row = int(input("What is the student's preferred row? "))
        pref_column = int(input("What is the student's preferred column? "))

    tables[pref_row-1][pref_column-1] = name

print("Here is the desired seating chart: \n\n")

for i in range(rows):
    for j in range(columns):
        print(tables[i][j], "\t")
    print()
