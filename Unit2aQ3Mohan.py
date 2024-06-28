# Name: Mohan Dixit
# Date: March 21st
# Purpose: Checks if the coins entered by the user equals $1

def check_total(number_of_nickels,number_of_dimes,number_of_quarters):

    # Calclulates the total sum of the coins
    total = number_of_nickels*0.05+number_of_dimes*0.1 + number_of_quarters*0.25

    # Prints the total
    print(format(total,'.2f'))

    # Checks to see if it is equal to, less than, or greater than 1
    if total == 1.0:
        print("Congratulations! You have won the game by getting exactly $1 using your coins!")
    elif total < 1.0:
        print(f"Oh no! Your coins fall short of the $1 needed to win the game!",
              f"You need ${1-total} more! Try again!")
    else:
        print(f"Oh no! Your coins add up to more than the $1 needed to win the game!",
              f"You need ${total-1} less! Try again!")    


def main():

    # Starting print statement

    print("Hello! You need to enter nickels, dimes, and quarters to reach $1!")

    
    # Gets the input: the number of nickels, dimes, and quarters
    
    number_of_nickels= int(input("Enter the number of nickels you have: "))
    number_of_dimes= int(input("Enter the number of dimes you have: "))
    number_of_quarters= int(input("Enter the number of quarters you have: "))


    nickel_total = number_of_nickels*0.05
    dime_total = number_of_dimes*0.1
    quarter_total = number_of_quarters*0.2

    
    # Prints out the number of each coin

    print(f"You have entered {number_of_nickels} nickels,",
          f"{number_of_dimes} dimes,",
          f"{number_of_quarters} quarters")

    # Prints out how much each coin adds up to

    print(f"\t{number_of_nickels} nickels = {number_of_nickels}*0.05 = $"+
          format(nickel_total,'.2f')+
          f"\n \t{number_of_dimes} dimes = {number_of_dimes}*0.1 = $"+
          format(dime_total,'.2f')+
          f"\n \t{number_of_quarters} quarters = {number_of_quarters}*0.25 = $"+
          format(quarter_total,'.2f'))

    # Adding print statement
    
    print("Adding these amounts together: \n",
          f"\t$" + format(nickel_total,'.2f') +  "(nickels) + ",
          f"$" + format(dime_total,'.2f') +  "(dimes) + ",
          f"$" + format(quarter_total,'.2f') +  "(quarters) = $", end='')


    # Calls function to calculate total
    check_total(number_of_nickels,number_of_dimes,number_of_quarters)

# Call the main function
main()

