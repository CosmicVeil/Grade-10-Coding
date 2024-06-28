import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
root = tk.Tk()
root.title("Math Question Generator")

score = 0

# Function to update the score display
def update_score_label():
    score_label.config(text=f"Score: {score}")

# Function to generate a new question based on the selected operation
def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = operation_var.get()

    if operation == "Addition":
        question = f"What is {num1} + {num2}?"
        correct_answer = num1 + num2
    elif operation == "Subtraction":
        question = f"What is {num1} - {num2}?"
        correct_answer = num1 - num2
    elif operation == "Multiplication":
        question = f"What is {num1} * {num2}?"
        correct_answer = num1 * num2
    elif operation == "Division":
        # Ensure no division by zero
        num2 = num2 if num2 != 0 else 1
        question = f"What is {num1} ÷ {num2}?"
        correct_answer = num1 // num2

    question_label.config(text=question)
    answer_entry.delete(0, tk.END)
    result_label.config(text="")
    return correct_answer

# Function to check the user's answer against the correct answer
def check_answer():
    global score
    try:
        user_answer = int(answer_entry.get())
        if user_answer == current_answer:
            score += 1
            result_label.config(text="Correct! Well done.")
        else:
            result_label.config(text=f"Incorrect! The correct answer was {current_answer}.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
    finally:
        update_score_label()


# Score display
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 16))
score_label.pack(anchor='ne')

# Dropdown for selecting operation
operation_var = tk.StringVar()
operation_var.set("Addition")  # default value
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
option_menu = tk.OptionMenu(root, operation_var, *operations)
option_menu.pack()

# Question label
question_label = tk.Label(root, text="Click 'Generate Question' to start.", font=("Arial", 14))
question_label.pack()

# Entry widget for entering answers
answer_entry = tk.Entry(root)
answer_entry.pack()

# Buttons
generate_button = tk.Button(root, text="Generate Question", command=lambda: generate_question())
generate_button.pack()

check_button = tk.Button(root, text="Check Answer", command=check_answer)
check_button.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# Initialize the first question
current_answer = generate_question()

root.mainloop()
