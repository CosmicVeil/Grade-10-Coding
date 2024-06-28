# Name: Mohan, Steven
# Purpose: Random Numbers

import random

def main():

    number = random.randint(1,10)
    print("Random number between 1-10:", number)

    for i in range(5):
        num2 = random.randint(1,100)
        print("Random number between 1-100:", num2)


main()