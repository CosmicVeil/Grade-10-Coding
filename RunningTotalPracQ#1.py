# Name: Mohan
# Purpose: Calc sum of of a week of sales 

MAX = 7

def main():
    total = 0
    print("You have to enter a week of sales, and this program will print out the sum")
    for counter in range(MAX):
        num = int(input("Enter a number: "))
        total += num
    
    print("The sum over the week is", total)

main()