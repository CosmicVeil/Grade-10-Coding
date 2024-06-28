# Name: Mohan Dixit
# Purpose: Geometry Calculator
# Date: Apr 11 2024

# Imports the other files
import triangle
import trapezoid


def main():


    # Runs the while loops until the user stops it
    while True:

        # Prints out the menu
        print("\n\n\nWelcome! This program can be used to calculate the",
            "area and perimeter of a triangle and trapezoid.")

        print("\nGeometry Calculator Menu:\n"+
            "\t1. Calculate the area of a triangle\n"+
            "\t2. Calculate the perimeter of a triangle\n"+
            "\t3. Calculate the area of a trapezoid\n"+
            "\t4. Calculate the perimeter of a trapezoid\n"+
            "\t5. Exit\n")
        

        # Asks for their choice
        choice = int(input("Enter your choice(1-5): "))

        # Checks if it is valid
        if choice < 1 or choice > 5:
            print("Invalid choice. Enter a value between 1-5")
        
        # Checks which choice the user chose, and accesses the correct module
        # to print out the correct output
        elif choice == 1:
            height = int(input("Enter the height of the triangle: "))
            base = int(input("Enter the base of the triangle: "))

            # Accesses triangle module
            area = triangle.area(base,height)
            print("The area of the triangle is:", area, "cm")
        elif choice == 2:
            side1 = int(input("Enter the first side of the triangle: "))
            side2 = int(input("Enter the second side of the triangle: "))
            side3 = int(input("Enter the third side of the triangle: "))
            
            # Accesses triangle module
            perimeter = triangle.perimeter(side1,side2,side3)
            print("The perimeter of the triangle is:", perimeter, "cm")
        elif choice == 3:
            top = int(input("Enter the value of the top-base: "))
            bottom = int(input("Enter the value of the bottom-base: "))
            height = int(input("Enter the height of the trapezoid: "))

            # Accesses trapezoid module
            area = trapezoid.area(top, bottom,height)
            print("The area of the trapezoid is:",area, "cm")
        elif choice == 4:
            side1 = int(input("Enter the first side of the trapezoid: "))
            side2 = int(input("Enter the second side of the trapezoid: "))
            side3 = int(input("Enter the third side of the trapezoid: "))
            side4 = int(input("Enter the fourth side of the trapezoid: "))
            
            # Accesses trapezoid module
            perimeter = trapezoid.perimeter(side1,side2,side3,side4)
            print("The perimeter of the trapezoid is:", perimeter, "cm")
        else:
            # If they enter 5, we break the loop
            break

main()