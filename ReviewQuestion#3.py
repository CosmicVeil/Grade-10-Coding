# Name: Mohan Dixit
# Date: March 20th
# Purpose: Enter tax and tip, and find the final answer


def solve(price, tax, tip):
    total = price+price*tax/100+price*tip/100

    # Calculate the total cost

    print("Total cost of the meal: $" +  format(total,'.2f'))
    
    

def main():


    print("Choose from the meals: \n",
          "- Hamburger $4\n",
          "- Cheese Sandwhich $3\n",
          "- Fries $2\n",
          "- Black Milkshake $1.5")

    works = True

    # Get input
    choice = input("Name of the meal: ").lower()
    tax_rate = float(input("Tax Rate: ")[0:-1])
    tip_rate = float(input("Tip Rate: ")[0:-1])

    if choice == "hamburger":
        cost = 4.5
    elif choice == "cheese sandwhich":
        cost = 4
    elif choice == "fries":
        cost = 3
    elif choice == "black milkshake":
        cost = 1.5
    else:
        print("Invalid Input, only the options are available")
        works = False


    # Call the function

    if works:
        solve(cost, tax_rate, tip_rate)

main()
