#Name: Mohan, Shawn
# Purpose: Calculate cost of diamonds
# Date: June 18th

def calculate_ring_cost(cost_per_karat):
    total_sparkling_cost = 0.0
    total_shiny_cost = 0.0

    while True:
        carat_sparkling = float(input("Enter the carat weight of the sparkling diamond: "))
        carat_shiny = float(input("Enter the carat weight of the shiny diamond: "))

        count_sparkling = int(input("Enter the count of the sparkling diamond: "))
        count_shiny = int(input("Enter the count of the shiny diamond: "))

        checkout = input("Are you ready to check out(y/n): ")

        if checkout.lower() == "y":
            cost_sparkling = 2.0*carat_sparkling + cost_per_karat
            cost_shiny= 1.5*carat_shiny + cost_per_karat

            total_sparkling_cost += cost_sparkling*count_sparkling
            total_shiny_cost += cost_shiny*count_shiny

            total_cost = total_sparkling_cost + total_shiny_cost

            print(f"The total cost is: {total_cost}")
            print(f"Sparkling Diamond Rings({count_sparkling}):"
                  f"${total_sparkling_cost:.2f}")
            print(f"Sparkling Diamond Rings({count_shiny}):"
                  f"${total_shiny_cost:.2f}")
        else:
            break

cost_per_carat = 500

calculate_ring_cost(cost_per_carat)