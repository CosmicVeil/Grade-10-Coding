# Name: Mohan Dixit
# Purpose: A math quiz and question generator
# Date: May 16th 2024


# Importing all the modules we need to run the program
from tkinter import *
import tkinter.messagebox as tkmb
import random
import questions


# These dictionaries contain the explanations and solutions to all problems
# We import it from the file questions.py
explanation_dict = questions.explanation_dict
solution_dict = questions.solution_dict
hint_dict = questions.hint_dict


# Lists of different topics and the questions
# We import it from the file questions.py
quadratics = questions.quadratics
basic_algebra = questions.basic_algebra
basic_math = questions.basic_math


# This class is the code for Practice Mode. This only runs when the user clicks the Practice Mode Button
class PracticeMode:

    def __init__(self, main):
        # Some variables that need to be accessed throughout the class
        self.correct = 0
        self.total = 0

        # Creates the window, the geometry, and sets the title
        self.root = Toplevel(main)
        self.root.geometry("400x500")
        self.root.title("Math Generator")
        self.root.config(bg='light blue')

        # Main frame for better organization and design
        frame = Frame(self.root, bg='light blue', padx=10, pady=10)
        frame.pack(fill='both', expand=True)
        
        # Creates the label to show the user's score
        self.score_label = Label(frame, text="Your score is: 0%", bg="light blue", fg="#000080", font=("Helvetica", 16))
        self.score_label.pack(anchor="ne")

        # This creates the drop-down menu, where the user can select a topic
        self.expl_label = Label(frame, text="Choose a topic for the next question: ", font=("Helvetica", 16), bg="light blue", fg="#000080")
        self.expl_label.pack(pady=(30,10))
        self.operation_var = StringVar()
        self.operation_var.set("Basic Algebra")  # default value
        self.operations = ["Basic Algebra", "Basic Math", "Quadratics"]
        self.option_menu = OptionMenu(frame, self.operation_var, *self.operations)
        self.option_menu.pack()



        # Question label
        self.question_label = Label(frame, text="Click 'Generate Question' to start.", font=("Helvetica", 17), bg="light blue", fg="#000080")
        self.question_label.pack(pady=(40,0))

        # Entry widget for entering answers
        self.answer_entry = Entry(frame, bg="grey")
        self.answer_entry.pack(pady=(0,50))

        # Buttons to generate a question and check the users answer
        self.generate_button = Button(frame, text="Generate Question", command=self.generate_question)
        self.generate_button.pack(pady=(0,20))

        self.check_button = Button(frame, text="Check Answer", command=self.check_answer)
        self.check_button.pack()

        # Hint button
        self.hint_button = Button(frame, text="Hint!", command=self.show_hint)
        self.hint_button.pack(pady=(20,20))

        # Quit button
        self.quit_button = Button(frame, text="Quit", command=self.root.destroy)
        self.quit_button.pack()

        # Initialize the first question
        self.generate_question()

    def generate_question(self):
        # Get the topic the user selected
        topic = self.operation_var.get()

        # Based on the topic we chose, we randomly chose a question from the respective list
        if topic == "Quadratics":
            self.question = random.choice(quadratics)
        elif topic == "Basic Math":
            self.question = random.choice(basic_math)
        elif topic == "Basic Algebra":
            self.question = random.choice(basic_algebra)

        # Set the question label to the question, and clear the answer entry box
        self.question_label.config(text=self.question)
        self.answer_entry.delete(0, END)

    def check_answer(self):
        # Gets the correct answer and the answer the user submitted
        given_answer = solution_dict[self.question]
        solution = self.answer_entry.get().replace(" ", "")  # Clears all excess whitespace

        # If nothing is entered, ask them to enter something
        if solution == "":
            tkmb.showinfo("Response", "Please enter an answer before submitting!")
            return

        # Check if they got the question right, update the answer print, and their score
        if solution == given_answer:
            answer_print = "Correct! Here is the way I did it: \n\t"
            self.correct += 1
        else:
            answer_print = "Incorrect! Here is how I did it: \n\t"

        # Create the answer print
        answer_print += f"{explanation_dict[self.question]}\n\n\n"

        # Create the window to tell the user if they got it right or wrong
        solution_window = Toplevel(self.root)
        solution_window.geometry("250x250")
        solution_window.title("Solutions")
        solution_window.config(bg="light blue")




        # Create the label in the window
        solutionLabel = Label(solution_window, text=answer_print, fg="#000080", bg="light blue", font=("Helvetica", 16)).pack()

        # Quit button
        self.quit_button = Button(solution_window, text="Quit", command=solution_window.destroy)
        self.quit_button.pack()

        # Update the user's percentage score
        self.total += 1
        self.update_score_label()
        self.generate_question()

    def show_hint(self):

        # Gets the hint from the questions using the hint dictionary
        hint_print = hint_dict[self.question]

        # Creates the new window for the hint
        hint_window = Toplevel(self.root)
        hint_window.geometry("700x100")
        hint_window.title("Hints")
        hint_window.config(bg="light blue")


        # Create the label in the window, which shows the hint
        hintLabel = Label(hint_window, text=hint_print, fg="#000080", bg="light blue", font=("Helvetica", 16)).pack()

        # Quit button
        self.quit_button = Button(hint_window, text="Quit", command=hint_window.destroy)
        self.quit_button.pack()


    def update_score_label(self):
        # Just changes the text in the score label
        my_text = "Score: " + str(int(self.correct / self.total * 100)) + "%"
        self.score_label.config(text=my_text)



# This class is the code for Quiz Mode. This only runs when the user clicks the Quiz Mode Button
class QuizMode:
    def __init__(self, main):

        # Initializes the global variables
        self.questions_list = []
        self.selected_questions = []
        self.started = False

        # Creates the window, sets the title and the geometry
        self.root = Toplevel(main)
        self.root.title("Math Question Generator")
        self.root.geometry("350x1100")


        # Main frame for the quiz
        self.frame = Frame(self.root, bg='light blue')
        self.frame.pack(expand=True, fill='both')


        # Radio buttons for selecting question type
        self.selected_bm = IntVar()
        self.selected_bm.set(0)  # default value
        self.selected_ba = IntVar()
        self.selected_ba.set(0)  # default value
        self.selected_q = IntVar()
        self.selected_q.set(0)  # default value


        # Creates a label explaining the check buttons, then creates the check buttons
        self.expl_label = Label(self.frame, text="Choose which topics you want for the quiz: ", font=("Helvetica", 16), bg="light blue", fg="#000080")
        self.expl_label.pack(pady=(30,10))
        Checkbutton(self.frame, text="Basic Math", variable=self.selected_bm, bg='light blue', fg="#000080", font=("Helvetica", 16)).pack()
        Checkbutton(self.frame, text="Basic Algebra", variable=self.selected_ba, bg='light blue', fg="#000080", font=("Helvetica", 16)).pack()
        Checkbutton(self.frame, text="Quadratics", variable=self.selected_q, bg='light blue', fg="#000080", font=("Helvetica", 16)).pack()
                
        # Button to start quiz
        start_quiz_button = Button(self.frame, text="Start Quiz", command=self.start_quiz)
        start_quiz_button.pack(pady=(20,20))

        # Display question and entry for answers
        self.entries = []
        self.question_labels = []

        # Initializes all the entries and labels in a nice for loop
        for _ in range(10):
            label = Label(self.frame, text="\n", bg='light blue', fg="#000080", font=("Helvetica", 15))
            label.pack()
            entry = Entry(self.frame)
            entry.pack()
            self.question_labels.append(label)
            self.entries.append(entry)


        # Submit button
        submit_button = Button(self.frame, text="Submit Answers", command=lambda: self.submit_answers(self.questions_list))
        submit_button.pack(pady=(20,20))

        # Quit button
        self.quit_button = Button(self.frame, text="Quit", command=self.root.destroy)
        self.quit_button.pack()

    # Function which runs when the user starts the quiz
    def start_quiz(self):

        # Check if the user has already started another quiz, and if they have, tell them to finish that one.
        if self.started:
            tkmb.showinfo("Response", "Finish the existing quiz before starting a new one!")
            return
        # Since the quiz started, we then set this var to true
        self.started = True

        # We check which one of the topics they want, and create a list where we add all of them together        
        if self.selected_q.get():
            self.questions_list.extend(quadratics)
        if self.selected_bm.get():
            self.questions_list.extend(basic_math)
        if self.selected_ba.get():
            self.questions_list.extend(basic_algebra)
        
        if not self.selected_ba.get() and not self.selected_bm.get() and not self.selected_q.get():
            tkmb.showinfo("Response", "Please chose a topic first!")
            return

        # Using a for loop we choose some questions
        for i in range(10):
            choice = random.choice(self.questions_list)
            my_text="\n"+choice
            self.selected_questions.append(choice)
            self.question_labels[i].config(text=my_text)
            self.entries[i].delete(0, END)


    def submit_answers(self, questions_list):
        # Keeps track of their score, and what they got wrong
        score = 0
        corrections = []

        # Check through the solutions and add to a string if they get something wrong
        for i, entry in enumerate(self.entries):
            if entry.get().replace(" ", "") == solution_dict[self.selected_questions[i]]:
                # If they get it right, add to the score
                score += 1
            else:
                # If the get it wrong, add some text to the corrections text
                corrections.append(f"Q{i+1}: {questions_list[i]}. \nHere is how I solved it: {explanation_dict[questions_list[i]]}\n")
        
        # Variable to store the score
        result_text = ""
        score_text = f"Score: {score}/10\n"

        # Check if they got everything right
        if corrections:
            result_text += "\nHere is what you got wrong:\n" + "\n".join(corrections)
        
        else:
            result_text += "\n\nWow! You passed with a perfect score!"

        # Create a window to print out the result text
        solution_window = Toplevel(self.root)
        solution_window.geometry("350x1100")
        solution_window.title("Solutions")
        solution_window.config(bg="light blue")

        # Create the label
        # Set started too false
        score_label = Label(solution_window, text=score_text,fg="#000080", bg="light blue", font=("Helvetica", 20)).pack()
        solutionLabel = Label(solution_window, text=result_text, fg="#000080", bg="light blue", font=("Helvetica", 14)).pack()
        self.started = False

        # Quit button
        self.quit_button = Button(solution_window, text="Quit", command=solution_window.destroy)
        self.quit_button.pack()

        # Set all the labels and entries to make them empty
        for i in range(10):
            self.question_labels[i].config(text="\n")
            self.entries[i].delete(0, END)



# This class is the code for the Info. This only runs when the user clicks the Info Button
class ShowInfo:
    def __init__(self, root):
        main = Toplevel(root)
        main.geometry("700x500")
        main.title("Info")
        
        # Main frame with a consistent background color
        frame = Frame(main, bg='light blue')
        frame.pack(expand=True, fill='both')

        myText = """Welcome to my math question generator!

My math question generator has two modes:

    - Practice Mode: Here you can practice your math knowledge, 
    by selecting a topic and getting questions relevant to that topic! 
    You can also check your answers, and your solve rate!

    - Quiz Mode: Here you can help hone your knowledge by taking part in a quiz.
    You just enter a topic, and the program generates you 10 questions!.
    As soon as you click the submit button, the program tells you your score, and what you got wrong!"""

        # Use a label with adjusted padding and font for better readability
        infoLabel = Label(frame, text=myText, bg='light blue', justify=LEFT, padx=20, pady=20, font=("Helvetica", 16), fg="#000080")
        infoLabel.pack(expand=True, fill='both')

        # Quit button
        self.quit_button = Button(frame, text="Quit", command=main.destroy, height=4, width=10)
        self.quit_button.pack()


# These functions just call the classes, and are run when the respective button is pressed
def runPracticeMode(main):
    PracticeMode(main)
def runQuizMode(main):
    QuizMode(main)
def runInfo(main):
    ShowInfo(main)


# Creates the main window, the title, and the size
root = Tk()
root.title("Math Questions by Mohan")
root.geometry("500x600")

# Add a bottom and top frame with a consistent background color
top_frame = Frame(root, bg='light blue')
top_frame.pack(expand=True, fill='both')
bottom_frame = Frame(root, bg='light blue')
bottom_frame.pack(fill='both')


# Creates a menu bar the user can use to access different parts of the app
menuBar = Menu(root)
root.config(menu=menuBar)


# Adds the options onto the bar
goToMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Go To", menu=goToMenu)
goToMenu.add_command(label="Practice Mode", command=lambda: runPracticeMode(root))
goToMenu.add_command(label="Quiz Mode", command=lambda: runQuizMode(root))


# More menu bar options
infoMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=infoMenu)
infoMenu.add_command(label="Info", command=lambda: runInfo(root))

# Creates the main label
mainLabel = Label(top_frame, text="MATH QUESTION AND QUIZZES\n\nBY MOHAN", fg="#000080", font=("Impact", 35, 'bold'), bg="light blue").pack(pady=(40,0))

# Creates the 4 buttons for each mode, and packs them
pracModeB = Button(bottom_frame, text="Practice Mode", command=lambda: runPracticeMode(root), height=4, width=15).pack(pady=(10,10))
quizModeB = Button(bottom_frame, text="Quiz Mode", command=lambda: runQuizMode(root), height=4, width=15).pack(pady=(10,10))
infoB = Button(bottom_frame, text="Info", command=lambda: runInfo(root), height=4, width=15).pack(pady=(10,10))
quizB = Button(bottom_frame, text="Quit", command=root.destroy, height=4, width=15).pack(pady=(10,10))

# Runs the program
root.mainloop()





