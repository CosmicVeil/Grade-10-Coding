# Name: Mohan, Steven
# Purpose: Area and Perimeter program

# Importing other programs
import square
import rhombus


# Menu:
print("Geometry Calculator Menu: ")
print("1. Calculate the area of a square")
print("2. Calculate the perimeter of a square")
print("3. Calculate the area of a rhombus")
print("4. Calculate the perimeter of a rhombus")
print("5. Quit")


# Loops runs untin user wants to stop it
while True:
    choice = int(input("Enter your choice: "))

    # Checks which option they want, and uses modules to find the answer
    if choice == 1:
        side = int(input("Enter the side length of the square: "))
        print("The area of the square is:", square.area(side))
    elif choice == 2:
        side = int(input("Enter the side length of the square: "))
        print("The perimeter of the square is:", square.perimeter(side))
    elif choice == 3:
        diag1 = int(input("Enter the length of diagonal one: "))
        diag2 = int(input("Enter the length of diagonal two: "))
        print("The area of the rhombus is:", rhombus.area(diag1,diag2))
    elif choice == 4:
        side = int(input("Enter the side length of the rhombus: "))
        print("The perimeter of the rhombus is:", rhombus.perimeter(side))
    elif choice == 5:
        break
    else:
        # If they don't enter a valid response, we print an error message
        print("Invalid choice!")