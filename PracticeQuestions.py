# Name: Mohan Dixit, and Hassaan Mir
# Date: March 6th 2024
# Purpose: Ask the user their name. Give a different message depending on
# whether they enter your (the programmer's) name or another name.
# In other words, write a program that compares the user's name to the
# programmer's name, and gives different messages depending on
# whether they are the same or different.

# Ask the user to enter two numbers, and have your program tell them
# which number is the larger of the two. Extend this program to also
# say if they are equal to each other.

# Ask the user to answer 3 math problems and either tell them they are
# right (IF), or show them the correct answer (ELSE). EXTEND (for
# more advanced programmers): Make this program more interesting
# by using random numbers.
import random

math_riddle = ["5*8/4+2", "5^2+6^2+7^2", "5*6*7+1", "6*7/14"]
math_riddle_answer = [5*8/4+2, 5**2+6**2+7**2, 5*6*7+1, 6*7/14]


def name_program():

    # Get input from user
    name = input("Enter your name: ")

    # Check my name
    if(name.lower() == "mohan"):
        print("Hey! That's my name!")

    # Check hassaan's name
    elif (name.lower() == "hassaan"):
        print("Hey! That's Hassaan name!")
    
    # Check the rest
    else:
        print("That's not us!")

def number_program():

    # Get both inputs
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))


    # Check if one is greater
    if(number_1 > number_2):
        print(f"{number_1} is bigger than {number_2}")
    
    # Check if they are equal
    elif(number_1 == number_2):
        print(f"{number_1} is equal than {number_2}")

    # Check if one is less
    else:
        print(f"{number_1} is smaller than {number_2}")


def math_problem_program():

    # Get a random riddle number
    riddle_num = random.randint(0,3)

    # Choose a riddle and answer
    print(math_riddle[riddle_num]);
    answer = float(input("Enter the answer: "))

    # Check if their answer is correct
    if answer == math_riddle_answer[riddle_num]:
        print("You're correct!")
    else:
        print(f"Incorrect! The correct answer is {math_riddle_answer[riddle_num]}")

def main():
    name_program()

    number_program()

    math_problem_program()