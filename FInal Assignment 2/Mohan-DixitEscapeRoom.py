# Name: Mohan Dixit
# Purpose: An escape room program, which the user can enjoy
# Date: June 4th

# Images:
#   https://cdn1.epicgames.com/ue/product/Screenshot/A15-1920x1080-5c5cff84362f4d5e4be0377fcc9b4c83.jpg?resize=1&w=1920

# Import necessary modules
import os
from tkinter import *
import tkinter.messagebox as tkmb
import random
import time
from PIL import Image, ImageTk
import questions  # Importing custom questions module

# Initialize game variables from questions module
curr_question = questions.curr_question  # Current main challenge question index
curr_quest = questions.curr_quest  # Current side quest index
num_incorrect = questions.num_incorrect  # Number of incorrect answers
time_left = questions.time_left  # Time left in milliseconds
gold = questions.gold  # Initial amount of gold
books_of_knowledge = questions.books_of_knowledge  # Initial number of books of knowledge

option_selected = questions.option_selected  # Initially selected option for side quests

# Initialize text and image prompts from questions module
challenge_text = questions.challenge_text
challenge_image = questions.challenge_image
challenge_answer = questions.challenge_answer
challenge_hint = questions.challenge_hint

# Initialize side quest data from questions module
sidequest_text = questions.sidequest_text
sidequest_image = questions.sidequest_image
sidequest_options = questions.sidequest_options
sidequest_answer = questions.sidequest_answer
sidequest_text_shown = questions.sidequest_text_shown

# Initialize ending text descriptions from questions module
ending_texts = questions.ending_texts
score = questions.score  # Initial score

print(len(challenge_text)+len(sidequest_text))
# Function to handle the countdown timer
def timer(remaining_seconds, tlabel, root):
    global time_left  # Use the global time_left variable
    remaining_minutes = remaining_seconds // 60000  # Calculate remaining minutes

    shown_seconds = int((remaining_seconds - remaining_minutes * 60000) / 1000)  # Calculate remaining seconds
    if shown_seconds < 10:
        shown_seconds = "0" + str(shown_seconds)  # Format seconds to always show two digits
    tlabel.config(text=f"Time Left: {remaining_minutes}:{shown_seconds}")  # Update the timer label
    if remaining_seconds < 0:
        tkmb.showinfo(title="Timeout", message="Time Limit Expired")  # Show timeout message
    else:
        time_left -= 1000  # Decrease the remaining time by 1 second
        root.after(1000, timer, time_left, tlabel, root)  # Schedule the function to run again in 1 second

# Function to display the player's stats at the end
def show_stats(root1):
    stats = f"""Stats:
    
                - Books of knowledge at the end of the game: {books_of_knowledge}
                - Gold at the end of the game: {gold}
                - Time taken: {int((300*1000-time_left)/1000)} seconds
                - Number of Incorrect: {num_incorrect}
                - Final Score: {score}, a score > 0 is good, 
                less than 0 and greater than -5 is decent
                and less than -5 is bad"""
    
    root = Toplevel(root1)  # Create a new window
    root.geometry("600x800")  # Set the window size
    root.title(f"Stats")  # Set the window title
    root.configure(bg="light blue")  # Set the background color

    stats_label = Label(root, text=stats, bg="light blue", font=("Helvetica", 20), fg="black").pack()  # Display the stats

# Function to display the ending of the game
def ending(root1, main):
    global time_left, books_of_knowledge, gold, num_incorrect, score
    time.sleep(0.1)  # Brief pause
    root1.withdraw()  # Hide the current window
    root = Toplevel(main)  # Create a new window
    root.geometry("600x800")  # Set the window size
    root.title(f"Ending")  # Set the window title
    root.configure(bg="light blue")  # Set the background color

    score = gold / 100 - num_incorrect  # Calculate the final score

    # Determine the ending text based on the score
    if score > 0:
        answer_text = ending_texts[0]
    elif score > -5:
        answer_text = ending_texts[1]
    else:
        answer_text = ending_texts[2]

    ending_label = Label(root, text=answer_text, fg="black", bg="light blue", font=("Helvetica", 20))  # Display the ending text
    ending_label.pack(pady=20)

    # Display the ending image
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    file_path = absolute_path + '/' + "ending.jpeg"
    img = ImageTk.PhotoImage(Image.open(file_path).convert('RGB').resize((300, 200)))
    panel = Label(master=root, image=img, bg="light blue")
    panel.img = img
    panel.pack()

    # Button to show stats
    stats_button = Button(root, text="Stats!", command=lambda: show_stats(root))
    stats_button.pack(pady=10)

    # Button to end the program
    close_button = Button(root, text="End program!", command=main.destroy)
    close_button.pack(pady=10)

# Function to test the user's answer for the current challenge
def test_value(value, root, main):
    global curr_question, num_incorrect
    print(value)  # Print the entered value for debugging
    if value == challenge_answer[curr_question]:  # Check if the answer is correct
        tkmb.showinfo("Result", "Correct!")  # Display correct message
        curr_question += 1  # Move to the next challenge
        if curr_question == 6:  # Check if all challenges are completed
            ending(root, main)  # Show the ending
        elif curr_question == 1 or curr_question == 5:  # Check if side quest should be generated
            generate_quest(main, root)
        else:
            generate_challenge(main, root)  # Generate the next challenge
    else:
        tkmb.showinfo("Result", "Wrong Answer! Try Again!")  # Display wrong answer message
        num_incorrect += 1  # Increment the number of incorrect answers

# Function to give a hint to the user
def give_hint(main, object_label):
    global books_of_knowledge
    root = Toplevel(main)  # Create a new window
    root.geometry("400x300")  # Set the window size
    root.title(f"Hint {curr_question+1}")  # Set the window title

    if books_of_knowledge <= 0:  # Check if user has enough books of knowledge
        hint_label = Label(root, text="You do not have enough books of knowledge!")  # Display message
        hint_label.pack()
    else:
        hint_label = Label(root, text=challenge_hint[curr_question])  # Display the hint
        hint_label.pack()
        books_of_knowledge -= 1  # Decrease the number of books of knowledge
        object_label.config(text=f"Inventory: {books_of_knowledge} Books of Knowledge, {gold} Gold")  # Update the inventory label

# Function to generate the main challenge
def generate_challenge(main, root1):
    global time_left, books_of_knowledge, gold
    time.sleep(0.1)  # Brief pause
    root1.destroy()  # Destroy the current window
    root = Toplevel(main)  # Create a new window
    root.geometry("600x800")  # Set the window size
    root.title(f"Challenge {curr_question+1}")  # Set the window title
    root.configure(bg="light blue")  # Set the background color

    # Create top frame with time and inventory labels
    top_frame = Frame(root, bg="light blue")
    time_label = Label(top_frame, bg="blue", font=("Helvetica", 16), text="Time Left: ", fg="white")
    objects_label = Label(top_frame, bg="blue", font=("Helvetica", 16), text=f"Inventory: {books_of_knowledge} Books of Knowledge, {gold} Gold")

    objects_label.pack(side="left", padx=(0,100))  # Pack inventory label to the left
    time_label.pack(side="right", padx=(100,0))  # Pack time label to the right
    top_frame.pack()

    timer(time_left, time_label, root)  # Start the timer

    entered_value = StringVar()  # Variable to store user input

    question_label = Label(root, text=challenge_text[curr_question], fg="black", bg="light blue", font=("Helvetica", 14))
    question_label.pack(pady=20)

    absolute_path = os.path.dirname(os.path.abspath(__file__))
    file_path = absolute_path + '/' + challenge_image[curr_question]
    img = ImageTk.PhotoImage(Image.open(file_path).convert('RGB').resize((300, 200)))
    panel = Label(master=root, image=img, bg="light blue")
    panel.img = img
    panel.pack()

    answer_entry = Entry(root, textvariable=entered_value, font=("Helvetica", 12))  # Entry for user input
    answer_entry.pack(pady=10)

    # Buttons to test the answer and give a hint
    test_button = Button(root, text="Test!", command=lambda: test_value(entered_value.get().lower(), root, main))
    hint_button = Button(root, text="Hint!", command=lambda: give_hint(root, objects_label))

    test_button.pack(pady=10)
    hint_button.pack(pady=10)

# Function to handle the next step after selecting a side quest option
def move_on(root, main):
    global books_of_knowledge, gold, curr_question, curr_quest, option_selected

    # Check which option the user selected, and update their inventory accordingly
    if option_selected == "option 1":
        books_of_knowledge = max(books_of_knowledge + sidequest_answer[curr_quest][0][0], 0)
        gold = max(gold + sidequest_answer[curr_quest][0][1], 0)
        tkmb.showinfo("Result", sidequest_text_shown[curr_quest][0])
    else:
        books_of_knowledge = max(books_of_knowledge + sidequest_answer[curr_quest][1][0], 0)
        gold = max(gold + sidequest_answer[curr_quest][1][1], 0)
        tkmb.showinfo("Result", sidequest_text_shown[curr_quest][1])
    # We are done with this quest, so we add 1
    curr_quest += 1
    # Reset option
    option_selected = "option 1"
    # After a quest, the next room is always a challenge room
    generate_challenge(main, root)

# Function to generate a side quest
def generate_quest(main, root1):
    global user_text, books_of_knowledge, gold
    time.sleep(0.1)  # Brief pause
    root1.destroy()  # Destroy the current window
    root = Toplevel(main)  # Create a new window
    root.geometry("600x600")  # Set the window size
    root.title(f"Side Quest {curr_quest+1}")  # Set the window title
    root.configure(bg="blue")  # Set the background color

    # Create top frame with time and inventory labels
    top_frame = Frame(root, bg="blue")
    time_label = Label(top_frame, bg="light blue", font=("Helvetica", 16), text="Time Left: ", fg="black")
    objects_label = Label(top_frame, bg="light blue", font=("Helvetica", 16), text=f"Inventory: {books_of_knowledge} Books of Knowledge, {gold} Gold", fg="black")

    objects_label.pack(side="left", padx=(0,100))  # Pack inventory label to the left
    time_label.pack(side="right", padx=(100,0))  # Pack time label to the right
    top_frame.pack()

    timer(time_left, time_label, root)  # Start the timer

    question_label = Label(root, text=sidequest_text[curr_quest], fg="black", bg="light blue", font=("Helvetica", 14))
    question_label.pack(pady=20)

    user_text = f"You selected: {sidequest_options[curr_quest][0]}"
    user_answer = Label(root, text=user_text, fg="black", bg="light blue")

    # Functions to handle option selection
    def opt1():
        global option_selected, user_text
        option_selected = "option 1"
        user_text = f"You selected: {sidequest_options[curr_quest][0]}"
        user_answer.config(text=user_text)

    def opt2():
        global option_selected
        option_selected = "option 2"
        user_text = f"You selected: {sidequest_options[curr_quest][1]}"
        user_answer.config(text=user_text)

    option1 = Button(root, text=sidequest_options[curr_quest][0], command=opt1, bg="red")
    option2 = Button(root, text=sidequest_options[curr_quest][1], command=opt2, bg="red")

    submit_button = Button(root, text="Next", command=lambda: move_on(root, main), bg="red")
    user_answer.pack()
    option1.pack(pady=(10,10))
    option2.pack()
    submit_button.pack(pady=(100,0))

# Function to start the program and choose a character
def start_program(main):
    global books_of_knowledge, gold
    main.withdraw()  # Hide the main window
    root = Toplevel(main)  # Create a new window
    root.geometry("600x500")  # Set the window size
    root.title("Choose your character")  # Set the window title
    root.configure(bg="blue")  # Set the background color

    character_var = "Your character: Wizard"
    info_label = Label(root, text=character_var, fg="white", bg="blue", font=("Helvetica", 14))
    info_label.pack(pady=20)

    books_of_knowledge = 1  # Default number of books of knowledge for Wizard
    gold = 0  # Default amount of gold for Wizard
    def update(opt):
        global books_of_knowledge, gold
        character_var = "Your character: " + opt
        info_label.config(text=character_var)
        if opt == "Wizard":
            books_of_knowledge = 1
            gold = 0
        else:
            books_of_knowledge = 0
            gold = 100

    wizard = Button(root, text="Wizard", command=lambda: update("Wizard"), bg="red", height=5, width=20)
    merchant = Button(root, text="Merchant", command=lambda: update("Merchant"), bg="red", height=5, width=20)

    wizard.pack()
    merchant.pack()

    submit_button = Button(root, text="Next", command=lambda: generate_challenge(main, root), fg="black", bg="red")
    submit_button.pack(pady=(100,0))

# Main function to start the application
def main():
    root = Tk()
    root.title("Lametis Escape")  # Set the window title
    root.geometry("800x500")  # Set the window size
    root.configure(background="light blue")  # Set the background color

    intro_label = Label(root, text="""You have been caught by the galactic soldiers and put in a cell,
                        all cause of that one day you decided to save the universe.

                        Of course, they capture you when you finally do something good. Drat!
                        
                        You try and gather all the information from your head: 

                        You are stuck on Lametis, a planet so despicable that even the worst villains fear it.
                                     To escape, you need to work together with your companions, Loki and his other self, Sylvie.
                        
                                     Here are some basic rules:
                        
                                        - As you go through the escape room, you will meet a certain challenge in front of you
                                        - If that challenge is solved, you get to move on
                                        - If its not, you will get to redo it
                                        - If you feel stuck, you can sacrifice a book of knowledge to get a hint,
                                             or even use some gold to skip the level entirely!""", fg="black", bg="light blue", font=("Helvetica", 16))
    intro_label.pack(anchor="center")

    start_button = Button(root, text="Start", command=lambda: start_program(root))
    start_button.pack()

    close_button = Button(root, text="Abort", command=root.destroy)
    close_button.pack()

    root.mainloop()

# Start the application
main()
