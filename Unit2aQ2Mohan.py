# Name: Mohan Dixit
# Date: March 21st
# Purpose: Find out the sot to paint a wall based on labor and paint in gallons


# This function gets all the values and calculates the total cost

def calc_cost(gallons_of_paint, hours_of_labor,cost_of_paint, labor_charges):

    
    total_cost = gallons_of_paint*cost_of_paint + hours_of_labor*labor_charges

    # Printing out the total cost

    print("The total cost of the paint job will be $" +  format(total_cost,'.2f'))



def main():

    # Getting the wall space and the price of paint of the user
    wall_space = int(input("Enter the square feet of wall needed to be painted: "))

    price_of_paint = float(input("Enter the price of one gallon of paint: "))

    
    # Calculating the number of gallons of paint needed, the hours of labor,
    # and the price of the labor per hour
    
    gallons_of_paint = wall_space/115
    hours_of_labor = wall_space/115*8
    labor_charges = 20

    
    # Printing out the basic output
    print(f"For {wall_space} square feet of wall space,",
          f"you will need: \n",
          f"\t", format(gallons_of_paint,'.2f'),"gallons of paint\n",
          f"\t", format(hours_of_labor,'.2f'),"hours of labor\n",
          f"\t $" + format(price_of_paint*gallons_of_paint,'.2f'), "of paint and",
          f"$" + format(hours_of_labor*labor_charges,'.2f'), "of labor charges")

    # Calling the function which calculates the total
    calc_cost(gallons_of_paint, hours_of_labor,price_of_paint, labor_charges)

main()
    
