# Name: Mohan
# Purpose: Calc sum of 10 numbers 

MAX = 7

def main():

    # Set accumilator to 0
    total = 0
    print("Enter the number of bugs you collected for each day of the week, and we will find the total")

    # For loop
    for counter in range(MAX):
        num = int(input("Enter the number of bugs you collected today: "))
        total += num
    
    # Print
    print("The number of bugs you collected in total is: ", total)

main()