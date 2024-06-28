MAX = 10

def main():
    total = 0
    print("You have to enter 10 numbers, and this program will print out the sum")
    for counter in range(MAX):
        num = int(input("Enter a number: "))
        total += num
    
    print("The sum is", total)

main()