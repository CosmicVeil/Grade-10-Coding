import random

# List to store riddles and their answers
riddles = ["What has to be broken before you can use it?", "I’m tall when I’m young, and I’m short when I’m old. What am I?", "What month of the year has 28 days?", "What is full of holes but still holds water?"]
riddle_answer = ["An egg", "A candle", "All of them","A sponge"]

math_riddle = ["5*8/4+2", "5^2+6^2+7^2", "5*6*7+1", "6*7/14"]
math_riddle_answer = [5*8/4+2, 5**2+6**2+7**2, 5*6*7+1, 6*7/14]


# Function which chooses random string riddle
def choose_string_riddle():
    riddle_num = random.randint(0,3)

    print(riddles[riddle_num]);
    answer = input("Enter the answer: ")

    if answer.lower() == riddle_answer[riddle_num]:
        print("You're correct!")
    else:
        print("Incorrect!")

# Function which chooses random math riddle
def choose_math_riddle():
    riddle_num = random.randint(0,3)

    print(math_riddle[riddle_num]);
    answer = float(input("Enter the answer: "))

    if answer == math_riddle_answer[riddle_num]:
        print("You're correct!")
    else:
        print("Incorrect!")

def main():

    # Keep running till user stops it
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
