# Name: Mohan Dixit
# Purpose: Guessing game for numbers
# Date: Apr 11 2024


import random
MAX = 15

def main():
    # Starter print statement
    print("This is ICD20's Number Guessing Game.",
        "(May test your IQ)")

    # Random multiple of 10 between 1 and 100
    answer = random.randint(1,10)*10

    # Number of attempts it took the user
    attempts = 0

    # While loop so they stay under 15 attempts
    while attempts < MAX:

        # Gets their guess and increments attempts
        guess = int(input("Guess the number between 1 and 100: "))
        attempts+=1

        # Validates input
        if guess > 100 or guess < 1:
            print("Please enter a valid number")
            # Since this is not a valid attempt, we subtract one, 
            # as we added one above
            attempts-=1
        elif guess%10 != 0:
            print("The number has to be a multiple of 10")
            # Same thng, as this is not a valid guess
            attempts-=1
        # Checks whether the number is correct
        elif guess > answer:
            print("Too high! Try again")
        elif guess < answer:
            print("Too Low! Try again")
        elif guess == answer:
            print(f"Congratulations! You are a genius! It only took you {attempts} guesses to get it!")
            break
        
    # If attempts is the same as 15, that means they went over the limit
    # So, we print out a you lost message
    if attempts == MAX:
        print("Oh no! You couldn't get the number!",
              f"The answer was {answer}!",
              "Better luck next time!")

main()