# Name: Mohan Dixit
# Purpose: An escape room program, which the user can enjoy
# Date: June 4th

# Images:
#   https://cdn1.epicgames.com/ue/product/Screenshot/A15-1920x1080-5c5cff84362f4d5e4be0377fcc9b4c83.jpg?resize=1&w=1920

# Import necessary modules
import os # User for accessing file access.
from tkinter import * # Used for tkinter
import tkinter.messagebox as tkmb # Used for messagr box
import time # Used for time
from PIL import Image, ImageTk # Used for images
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

timer_done = False


def typewriter_effect(label, text, index=0):
        # Display text one character at a time to create a typewriter effect
        if index < len(text):
            label.config(text=label.cget("text") + text[index])
            index += 1
            label.after(50, typewriter_effect, label, text, index)

# Function to handle the countdown timer
def timer(remaining_seconds, tlabel, root):
    global time_left  # Use the global time_left variable
    remaining_minutes = remaining_seconds // 60000  # Calculate remaining minutes

    shown_seconds = int((remaining_seconds - remaining_minutes * 60000) / 1000)  # Calculate remaining seconds
    if shown_seconds < 10:
        shown_seconds = "0" + str(shown_seconds)  # Format seconds to always show two digits
    tlabel.config(text=f"Time Left: {remaining_minutes}:{shown_seconds}")  # Update the timer label
    if remaining_seconds < 0:
        tkmb.showinfo(title="Timeout", message="Time Limit Expired. You lose!\nYou will still be able to finish the escape room, though! ")  # Show timeout message
        timer_done = True
    else:
        time_left -= 1000  # Decrease the remaining time by 1 second
        root.after(1000, timer, time_left, tlabel, root)  # Schedule the function to run again in 1 second

# Function to display the player's stats at the end
def show_stats(root1):
    stats = f"""
    Stats:
    
    Books of Knowledge at the end of the game: {books_of_knowledge}
    Gold at the end of the game: {gold}
    Time taken: {int((600*1000-time_left)/1000)} seconds
    Number of Incorrect Answers: {num_incorrect}
    Final Score: {score}

    Score Evaluation:
    - A score > 0 is good
    - A score between 0 and -5 is decent
    - A score < -5 is bad
"""

    root = Toplevel(root1)  # Create a new window
    root.geometry("600x800")  # Set the window size
    root.title("Game Stats")  # Set the window title
    root.configure(bg="#f5f5f5")  # Set the background color

    # Create a frame to hold the stats
    stats_frame = Frame(root, bg="#f5f5f5", padx=20, pady=20)
    stats_frame.pack(expand=True)

    # Display the stats with better formatting
    Label(stats_frame, text="Game Statistics", bg="#f5f5f5", font=("Helvetica", 24, "bold"), fg="black").pack(pady=(0, 20))
    Label(stats_frame, text=f"Books of Knowledge: {books_of_knowledge}", bg="#f5f5f5", font=("Helvetica", 18), fg="black").pack(anchor="w")
    Label(stats_frame, text=f"Gold: {gold}", bg="#f5f5f5", font=("Helvetica", 18), fg="black").pack(anchor="w")
    Label(stats_frame, text=f"Time Taken: {int((600*1000-time_left)/1000)} seconds", bg="#f5f5f5", font=("Helvetica", 18), fg="black").pack(anchor="w")
    Label(stats_frame, text=f"Incorrect Answers: {num_incorrect}", bg="#f5f5f5", font=("Helvetica", 18), fg="black").pack(anchor="w")
    Label(stats_frame, text=f"Final Score: {score}", bg="#f5f5f5", font=("Helvetica", 18), fg="black").pack(anchor="w")

    # Score evaluation section
    Label(stats_frame, text="Score Evaluation:", bg="#f5f5f5", font=("Helvetica", 20, "bold"), fg="black").pack(pady=(20, 10))
    Label(stats_frame, text="- A score > 0 is good", bg="#f5f5f5", font=("Helvetica", 16), fg="black").pack(anchor="w")
    Label(stats_frame, text="- A score between 0 and -5 is decent", bg="#f5f5f5", font=("Helvetica", 16), fg="black").pack(anchor="w")
    Label(stats_frame, text="- A score < -5 is bad", bg="#f5f5f5", font=("Helvetica", 16), fg="black").pack(anchor="w")


# Function to display the ending of the game
def ending(root1, main):
    global time_left, books_of_knowledge, gold, num_incorrect, score
    time.sleep(0.1)  # Brief pause
    root1.withdraw()  # Hide the current window
    root = Toplevel(main)  # Create a new window
    root.geometry("600x800")  # Set the window size
    root.title(f"Ending")  # Set the window title
    root.configure(bg="#f5f5f5")  # Set the background color

    if timer_done == False: # If they ran out of time, they always get the bad ending.
        score = gold / 50 - num_incorrect  # Calculate the final score
    else:
        score = -10  # Score which corresponds to a bad ending

    # Determine the ending text based on the score
    if score > 0:
        answer_text = ending_texts[0]
    elif score > -5:
        answer_text = ending_texts[1]
    else:
        answer_text = ending_texts[2]

    ending_label = Label(root, text="", fg="black", bg="#f5f5f5", font=("Helvetica", 20))  # Display the ending text
    ending_label.pack(pady=20)

    # Add the text
    typewriter_effect(ending_label, answer_text)

    # Display the ending image
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    file_path = absolute_path + '/' + "ending.jpeg"
    img = ImageTk.PhotoImage(Image.open(file_path).convert('RGB').resize((300, 200)))
    panel = Label(master=root, image=img, bg="#f5f5f5")
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
    root.configure(bg="#f5f5f5")  # Set the background color

    # Create top frame with time and inventory labels
    top_frame = Frame(root, bg="#f5f5f5")
    time_label = Label(top_frame, bg="#008080", font=("Helvetica", 16), text="Time Left: ", fg="white")
    objects_label = Label(top_frame, bg="#008080", font=("Helvetica", 16), text=f"Inventory: {books_of_knowledge} Books of Knowledge, {gold} Gold")

    objects_label.pack(side="left", padx=(0,100))  # Pack inventory label to the left
    time_label.pack(side="right", padx=(100,0))  # Pack time label to the right
    top_frame.pack()

    timer(time_left, time_label, root)  # Start the timer

    entered_value = StringVar()  # Variable to store user input

    # Add the question with the type writer effect
    question_label = Label(root, text="", fg="black", bg="#f5f5f5", font=("Helvetica", 14))
    question_label.pack(pady=20)
    typewriter_effect(question_label, challenge_text[curr_question])


    # Add an image
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    file_path = absolute_path + '/' + challenge_image[curr_question]
    img = ImageTk.PhotoImage(Image.open(file_path).convert('RGB').resize((300, 200)))
    panel = Label(master=root, image=img, bg="#f5f5f5")
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
    root.configure(bg="#008080")  # Set the background color

    # Create top frame with time and inventory labels
    top_frame = Frame(root, bg="#008080")
    time_label = Label(top_frame, bg="#f5f5f5", font=("Helvetica", 16), text="Time Left: ", fg="black")
    objects_label = Label(top_frame, bg="#f5f5f5", font=("Helvetica", 16), text=f"Inventory: {books_of_knowledge} Books of Knowledge, {gold} Gold", fg="black")

    objects_label.pack(side="left", padx=(0,100))  # Pack inventory label to the left
    time_label.pack(side="right", padx=(100,0))  # Pack time label to the right
    top_frame.pack()

    timer(time_left, time_label, root)  # Start the timer


    # Create a question label, with the type writer effect
    question_label = Label(root, text="", fg="black", bg="#f5f5f5", font=("Helvetica", 14))
    question_label.pack(pady=20)
    typewriter_effect(question_label, sidequest_text[curr_quest])

    # Create a option where it shows the user what they selected
    user_text = f"You selected: {sidequest_options[curr_quest][0]}"
    user_answer = Label(root, text=user_text, fg="black", bg="#f5f5f5")

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

    # Create the option buttons
    option1 = Button(root, text=sidequest_options[curr_quest][0], command=opt1)
    option2 = Button(root, text=sidequest_options[curr_quest][1], command=opt2)

    
# Create the submit buttons and pack everything
    submit_button = Button(root, text="Next", command=lambda: move_on(root, main))
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
    root.configure(bg="#008080")  # Set the background color

    # Create the label which shows the user the character they chose
    character_var = "Your character: Wizard"
    info_label = Label(root, text=character_var, fg="white", bg="#008080", font=("Helvetica", 14))
    info_label.pack(pady=20)

    books_of_knowledge = 1  # Default number of books of knowledge for Wizard
    gold = 0  # Default amount of gold for Wizard
    def update(opt):
        # Updates the books of knowledge and gold based on what they click
        global books_of_knowledge, gold
        character_var = "Your character: " + opt
        info_label.config(text=character_var)
        if opt == "Wizard":
            books_of_knowledge = 1
            gold = 0
        else:
            books_of_knowledge = 0
            gold = 100


    # Creates the buttons for the choices
    wizard = Button(root, text="Wizard", command=lambda: update("Wizard"),  height=5, width=20)
    merchant = Button(root, text="Merchant", command=lambda: update("Merchant"), height=5, width=20)

    # Packs the button
    wizard.pack()
    merchant.pack()


    # Creates the submit button and packs it
    submit_button = Button(root, text="Next", command=lambda: generate_challenge(main, root), fg="black")
    submit_button.pack(pady=(100,0))

# Main function to start the application
def main():
    root = Tk()
    root.title("Lametis Escape")  # Set the window title
    root.geometry("800x900")  # Set the window size
    root.configure(background="#f5f5f5")  # Set the background color

    # Create the title label
    title_label = Label(root, text="Lamentis Escape", font=("Impact", 50), bg="#f5f5f5", fg='black')
    # Create the main label
    intro_label = Label(root, text=
                        "", fg="black", bg="#f5f5f5", font=("Helvetica", 16))
    
    typewriter_effect(intro_label, """You have been caught by the galactic soldiers and put in a cell,
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
                or even use some gold to skip the level entirely!
                - Sometimes you will get quest windows.
                - Here, you don't have to answer a question, but the option you choose,
                can completely change the escape room!
                
                The windows are distinguished by color.
                Light Grey is a challenge window,
                and Teal is a quest window!""")
    title_label.pack()
    intro_label.pack(anchor="center", pady=(100,0))

    # Create the start and abort buttons, and pack them
    start_button = Button(root, text="Start", command=lambda: start_program(root))
    start_button.pack(pady=(100,0))

    close_button = Button(root, text="Abort", command=root.destroy)
    close_button.pack()

    root.mainloop()

# Start the application
main()
