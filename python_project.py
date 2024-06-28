import random

riddles = ["What has to be broken before you can use it?", "I’m tall when I’m young, and I’m short when I’m old. What am I?", "What month of the year has 28 days?", "What is full of holes but still holds water?"]
riddle_answer = ["An egg", "A candle", "All of them","A sponge"]

math_riddle = ["Using only addition, add eight 8s to get the number 1,000.", "I add six to eleven, and get five. Why is this correct?", "What single digit appears most frequently between and including the numbers 1 and 1,000? Hint: Look for a pattern!"]
math_riddle_answer = ["888 + 88 + 8 + 8 + 8 = 1,000.", "When it is 11 a.m., adding six hours makes it 5 p.m.", "The most common digit is 1!"]

def choose_string_riddle():
    riddle_num = random.randint(0,4)

    print(riddles[riddle_num]);
    answer = input("Enter the answer: ")

    if answer.lower() == riddle_answer[riddle_num]:
        print("You're correct!")
    else:
        print("Incorrect!")


def choose_math_riddle():
    riddle_num = random.randint(0,4)

    print(math_riddle[riddle_num]);
    answer = input("Enter the answer: ")

    if answer.lower() == math_riddle_answer[riddle_num]:
        print("You're correct!")
    else:
        print("Incorrect!")

def main():

    while True:

        keep_running = input("Do you want another riddle(Type math for a math riddle, yes for a normal riddle, no to end the program): ")

        if(keep_running.lower() == "no"):
            break
        elif keep_running.lower() == "math":
            choose_math_riddle()
        else:
            choose_string_riddle()
    
    print("\nProgram ended!")

main()
