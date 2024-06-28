
from tkinter import *
import tkinter.messagebox as tkmb
import random



question = ""
correct = 0
total = 0

root = Tk()
root.geometry("400x500")
root.title("Math Generator")


explanation_dict = {"2x + 8 = 6": "\n 2x=-2\n x=-1",
    "3x + 2 = 5x + 6": "\n 5x-3x = 2-6\n 2x = -4\n x=-2",
    "x + 3x + 4x = 1 + 3 + 4": "\n 8x = 8\n x=1",
    "3x + 2x + 8 = -2": "\n5x=-10\nx=-2",
    "x/7 = 21": "\nx=21*7\nx=147",
    "x/7 + 7 = x/5 + 5": "\n2/35x=2\nx=2*35/2\nx=35",
    "x/3 + x/3 = 2/3": "2/3x = 2/3\nx=1",
    "3y + 4y = y + 5y + 7": "7y = 6y + 7\ny=7",
    "3x + 7 + 4x = 9x = 11": "7x + 7 = 9x - 11\n2x=7+11\nx=9",
    "5x = 10":"x=10/2\nx=5",
    "Find the sum of the two roots. x^2 + 5x + 6 = 0": "\n(x+3)(x+2)\n\tx=-2,-3\nSo, the sum is: -2+(-3) = -5",
    "Find the sum of the two roots. x^2 + 6x + 5 = 0": "\n(x+5)(x+1)\n\tx=-1,-5\nSo, the sum is: -1+(-1) = -6",
    "Find the sum of the two roots. x^2 - 12x + 16 = 0": "\n(x-8)(x-4)\n\tx=4,8\nSo, the sum is: 4+8 = 12",
    "Find the sum of the two roots. 3x^2 + 16x + 20 = 0": "\n(3x+10)(x+2)\n\tx=-10/3,-2\nSo, the sum is: -2+(-10/3) = -16/3",
    "Find the sum of the two roots. 5x^2 - 23x + 12 = 0": "\n(5x-3)(x-4)\n\tx=4,3/5\nSo, the sum is: 4+(3/5) = 23/5",
    "Find the sum of the two roots. x^2 - 3x - 4 = 0": "\n(x-4)(x+1)\n\tx=4,-1\nSo, the sum is: 4+(-1) = -3",
    "Find the sum of the two roots. 2x^2 + 8x + 6 = 0": "\n2(x+3)(x+1)\n\tx=-3,-1\nSo, the sum is: -3+(-1) = -4",
    "Find the sum of the two roots. x^2 - 5x + 6 = 0": "\n(x-3)(x-2)\n\tx=2,3\nSo, the sum is: 2+3 = 5",
    "Find the sum of the two roots. 3x^2 - 6x - 9 = 0": "\n3(x-3)(x+1)\n\tx=3,-1\nSo, the sum is: 3+(-1) = 2",
    "Find the sum of the two roots. x^2 + 2x - 8 = 0": "\n(x+4)(x-2)\n\tx=-4,2\nSo, the sum is: -4+2 = -2",
    "Find the sum of the two roots. x^2 - 7x + 12 = 0": "\n(x-3)(x-4)\n\tx=3,4\nSo, the sum is: 3+4 = 7",
    "Find the sum of the two roots. 4x^2 + 16x + 15 = 0": "\n(x+3)(x+2)\n\tx=-2,-3\nSo, the sum is: -2+(-3) = -5",
    "Find the sum of the two roots. x^2 - 8x + 15 = 0": "\n(x-5)(x-3)\n\tx=5,3\nSo, the sum is: 5+3 = 8",
    "Find the sum of the two roots. 5x^2 + 5x - 30 = 0": "\n5(x+6)(x-5)\n\tx=-6,5\nSo, the sum is: -6+5 = -1",
    "Find the sum of the two roots. 2x^2 - 12x + 16 = 0": "\n2(x-4)(x-2)\n\tx=2,4\nSo, the sum is: 2+4 = 6", 
}
solution_dict = {
    "Find the sum of the two roots. x^2 + 5x + 6 = 0": "-5",
    "Find the sum of the two roots. x^2 + 6x + 5 = 0": "-6",
    "Find the sum of the two roots. x^2 - 12x + 16 = 0": "6",
    "Find the sum of the two roots. 3x^2 + 16x + 20 = 0": "-16/3",
    "Find the sum of the two roots. 5x^2 - 23x + 12 = 0": "23/5",
    "Find the sum of the two roots. x^2 - 3x - 4 = 0": "3",
    "Find the sum of the two roots. 2x^2 + 8x + 6 = 0": "-4",
    "Find the sum of the two roots. x^2 - 5x + 6 = 0": "5",
    "Find the sum of the two roots. 3x^2 - 6x - 9 = 0": "2",
    "Find the sum of the two roots. x^2 + 2x - 8 = 0": "-2",
    "Find the sum of the two roots. x^2 - 7x + 12 = 0": "7",
    "Find the sum of the two roots. 4x^2 + 16x + 15 = 0": "-4",
    "Find the sum of the two roots. x^2 - 8x + 15 = 0": "-8",
    "Find the sum of the two roots. 5x^2 + 5x - 30 = 0": "-1",
    "Find the sum of the two roots. x^2 + 6x + 5 = 0": "-6", 
    "Find the sum of the two roots. 2x^2 - 12x + 16 = 0": "6", 
    "Find the sum of the two roots. 3x^2 + 16x + 20 = 0": "-16/3", 
    "Find the sum of the two roots. 5x^2 - 23x + 12 = 0": "17/5",
    "2x + 8 = 6": "x=-1",
    "3x + 2 = 5x + 6": "x=-2",
    "x + 3x + 4x = 1 + 3 + 4": "x=1",
    "3x + 2x + 8 = -2": "x=-2",
    "x/7 = 21": "x=147",
    "x/7 + 7 = x/5 + 5": "x=35",
    "x/3 + x/3 = 2/3": "x=1",
    "3y + 4y = y + 5y + 7": "y=7",
    "3x + 7 + 4x = 9x = 11": "x=-2",
    "5x = 10":"x=2",
    "Find the derivative: f(x) = x^2": "f'(x) = 2x",
    "Find the derivative: f(x) = 3x^3": "f'(x) = 9x^2",
    "Find the derivative: f(x) = 4x": "f'(x) = 4",
    "Find the derivative: f(x) = 5x^5": "f'(x) = 25x^4",
    "Find the derivative: f(x) = 6x^2 + 3x": "f'(x) = 12x + 3",
    "Find the derivative: f(x) = 7x^4 - x^2": "f'(x) = 28x^3 - 2x",
    "Find the derivative: f(x) = 8x^3 + 2x^2": "f'(x) = 24x^2 + 4x",
    "Find the derivative: f(x) = sin(x)": "f'(x) = cos(x)",
    "Find the derivative: f(x) = cos(x)": "f'(x) = -sin(x)",
    "Find the derivative: f(x) = e^x": "f'(x) = e^x",
    "Find the derivative: f(x) = ln(x)": "f'(x) = 1/x",
    "Find the derivative: f(x) = tan(x)": "f'(x) = sec^2(x)",
    "Find the derivative: f(x) = sec(x)": "f'(x) = sec(x)tan(x)",
    "Find the derivative: f(x) = csc(x)": "f'(x) = -csc(x)cot(x)",
    "Find the derivative: f(x) = cot(x)": "f'(x) = -csc^2(x)",
    "Find the derivative: f(x) = sqrt(x)": "f'(x) = 1/(2sqrt(x))",
    "Find the derivative: f(x) = 1/x": "f'(x) = -1/x^2",
    "Find the derivative: f(x) = x^(-2)": "f'(x) = -2x^(-3)",
    "Find the derivative: f(x) = 3x^2 + 5x - 2": "f'(x) = 6x + 5",
    "Find the derivative: f(x) = 4x^3 - 3x + 6": "f'(x) = 12x^2 - 3",
    "Find the derivative: f(x) = 5x^4 + 10x^3 - x": "f'(x) = 20x^3 + 30x^2 - 1",
    "Find the derivative: f(x) = 6x^5 - 4x^3 + 2x - 1": "f'(x) = 30x^4 - 12x^2 + 2",
    "Find the derivative: f(x) = e^(2x)": "f'(x) = 2e^(2x)",
    "Find the derivative: f(x) = x^2 * ln(x)": "f'(x) = 2x*ln(x) + x",
    "Find the derivative: f(x) = (x^3 + 1) / (x^2 - 1)": "f'(x) = ((3x^2)(x^2 - 1) - (x^3 + 1)(2x)) / (x^2 - 1)^2",
    "100*100*100": "1000000",
    "(1+2)*3": "9",
    "(2+4)/2+6": "9",
    "(10+10)/10+10": "12",
    "4*4*4/2": "32",
    "19+31+50/10": "55",
    "(10/5+1)*6": "18",
    "99*2+1": "199",
    "(1+1+1+1)*0": "0",
    "1+1+1+1*0" : "3"
}


# Lists of different topics and the questions
quadratics = ["Find the sum of the two roots. x^2 + 5x + 6 = 0", "Find the sum of the two roots. x^2 + 6x + 5 = 0", "Find the sum of the two roots. 2x^2 - 12x + 16 = 0", "Find the sum of the two roots. 3x^2 + 16x + 20 = 0", "Find the sum of the two roots. 5x^2 - 23x + 12 = 0", "Find the sum of the two roots. x^2 + 6x + 5 = 0",
    "Find the sum of the two roots. x^2 - 3x - 4 = 0",
    "Find the sum of the two roots. 2x^2 + 8x + 6 = 0",
    "Find the sum of the two roots. x^2 - 5x + 6 = 0",
    "Find the sum of the two roots. 3x^2 - 6x - 9 = 0",
    "Find the sum of the two roots. x^2 + 2x - 8 = 0",
    "Find the sum of the two roots. x^2 - 7x + 12 = 0",
    "Find the sum of the two roots. 4x^2 + 16x + 15 = 0",
    "Find the sum of the two roots. x^2 - 8x + 15 = 0",
    "Find the sum of the two roots. 5x^2 + 5x - 30 = 0",
]
basic_algebra = [
    "2x + 8 = 6",
    "3x + 2 = 5x + 6",
    "x + 3x + 4x = 1 + 3 + 4",
    "3x + 2x + 8 = -2",
    "x/7 = 21",
    "x/7 + 7 = x/5 + 5",
    "x/3 + x/3 = 2/3",
    "3y + 4y = y + 5y + 7",
    "3x + 7 + 4x = 9x + 11",
    "5x = 10"
]
basic_math = ["(1+2)*3", "(2+4)/2+6", "(10+10)/10+10", "4*4*4/2", "19+31+50/10", "100*100*100", "(10/5+1)*6", "99*2+1", "(1+1+1+1)*0", "1+1+1+1*0"]

operation_var = StringVar()
operation_var.set("Basic Algebra")  # default value
operations = ["Basic Algebra", "Basic Math", "Quadratics"]
option_menu = OptionMenu(root, operation_var, *operations)
option_menu.pack()

start = True

def generate_question():
    global question, start
    topic = operation_var.get()

    if answer_entry.get() == "" and not start:
        tkmb.showinfo("Response", "Please solve this question before moving on!")
        return

    # Based on the topic we chose, we randomly chose a value from the respective list
    if topic == "Quadratics":
        question = random.choice(quadratics)
    elif topic == "Basic Math":
        question = random.choice(basic_math)
    elif topic == "Basic Algebra":
        question = random.choice(basic_algebra)

    question_label.config(text=question)
    answer_entry.delete(0, END)
    result_label.config(text="")

    start= FALSE
    #return correct_answer


def check_answer():
    global correct, total

    given_answer = solution_dict[question]

    solution = answer_entry.get()
    answer_print = ""

    if solution == given_answer:
        answer_print = "Correct! Here is the way I did it: \n\t"
        correct+=1
    else:
        answer_print = "Incorrect! Here is how I did it: \n\t"

    answer_print+= f"{explanation_dict[question]}\n\n\n"

    total+=1
    update_score_label()

    tkmb.showinfo("Response", answer_print)

    generate_question()


def update_score_label():
    global correct, total
    my_text = "Score: " + str(int(correct/total*100)) + "%"
    score_label.config(text=my_text)

score_label = Label(root, text = f"Your score is: 0%")
score_label.pack(anchor="ne")

# Question label
question_label = Label(root, text="Click 'Generate Question' to start.", font=("Arial", 14))
question_label.pack()

# Entry widget for entering answers
answer_entry = Entry(root)
answer_entry.pack()

# Buttons
generate_button = Button(root, text="Generate Question", command=generate_question)
generate_button.pack()

check_button = Button(root, text="Check Answer", command=check_answer)
check_button.pack()

# Result label
result_label = Label(root, text="", font=("Arial", 14))
result_label.pack()

# Initialize the first question
current_answer = generate_question()

root.mainloop()




