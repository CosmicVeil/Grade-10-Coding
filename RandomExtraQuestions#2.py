#Name: Mohan, Steven
#  Purpose: Random

import random

number = random.randint(1,100)

def g():
    guess = int(input("guess 1-100:"))

    if guess > number:
        print("too high")
        g()
    elif guess < number:
        print('too low')
        g()
    elif guess == number:
        print("correct")
        
g()



