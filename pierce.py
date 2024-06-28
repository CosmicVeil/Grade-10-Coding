from tkinter import *
from tkinter import messagebox
import random

main_window = Tk()
main_window.title = ("Rock,Paper,Scissors")
main_window.geometry = ("1000x600")

user_label = Label(main_window, text = "User choice:")
computer_label = Label(main_window, text = "Computer's Choice:") 
Result = Label(main_window, text = "Results:")
user_choice = Entry(main_window)
computer_choice = Entry(main_window)




def command(choice):
    #user_choice.get()
    user_choice.delete(0,END)
    user_choice.insert(0,str(choice))

def check_if_win():
    #computer_choice.get()
    computer_choice.delete(0,END)        
    computer_choice.insert(0,str(random.choice(["Scissors","Rock","Paper"])))
    if user_choice.get().strip()  == 'Paper' and computer_choice.get().strip()  == "Scissors":
        loss = Label(main_window, text = "You lost. You chose Paper, while the computer chose Scissors.", fg = "red")
        loss.grid(row = 10, column = 6, columnspan = 2)
    elif user_choice.get().strip()  == "Paper" and computer_choice.get().strip()  == "Rock":
        won = Label(main_window, text = "You won! You chose Paper, while the computer chose Rock.", fg = "green")
        won.grid(row = 10, column = 6, columnspan = 2)
    elif user_choice.get().strip()  == 'Scissors' and computer_choice.get().strip()  == "Rock":
        loss = Label(main_window, text = "You lost. You chose Scissors, while the computer chose Rock.", fg = "red")
        loss.grid(row = 10, column = 6, columnspan = 2)
    elif user_choice.get().strip()  == "Scissors" and computer_choice.get().strip()  == "Paper":
        won = Label(main_window, text = "You won! You chose Scissors, while the computer chose Paper.", fg = "green")
        won.grid(row = 10, column = 6, columnspan = 2)
    elif user_choice.get().strip()  == "Rock" and computer_choice.get().strip()  == "Paper":
        loss = Label(main_window, text = "You lost! You chose Rock, while the computer chose Paper.", fg = "red")
        loss.grid(row = 10, column = 6, columnspan = 2)
    elif user_choice.get().strip()  == "Rock" and computer_choice.get().strip()  == "Scissors":
        won = Label(main_window, text = "You won! You chose Rock, while the computer chose Scissors.", fg = "green")
        won.grid(row = 10, column = 6, columnspan = 2)
    elif user_choice.get().strip()  == "Scissors" and computer_choice.get().strip()  == "Scissors":
        draw = Label(main_window, text = "It's a tie! You chose Scissors, while the computer also chose Scissors.", fg = "grey")
        draw.grid(row = 10, column = 6, columnspan = 2)
    elif user_choice.get().strip()  == "Paper" and computer_choice.get().strip()  == "Paper":
        draw = Label(main_window, text = "It's a tie! You chose Paper, while the computer also chose Paper.", fg = "grey")
        draw.grid(row = 10, column = 6, columnspan = 2)
    elif user_choice.get().strip()  == "Rock" and computer_choice.get().strip()  == "Rock":
        draw = Label(main_window, text = "It's a tie! You chose Rock, while the computer also chose Rock.", fg = "grey")
        draw.grid(row = 10, column = 6, columnspan = 2)

Rock = Button(main_window, text = "Rock", command = lambda: command("Rock"))
Paper = Button(main_window, text = "Paper", command = lambda:command("Paper"))
Scissors = Button(main_window, text = "Scissors", command = lambda:command("Scissors"))
Submit_button = Button(main_window, text = "Submit", command = check_if_win)

user_label.grid(row=4, column = 5)
computer_label.grid(row=4, column = 6)
user_choice.grid(row =5, column = 5)
computer_choice.grid(row =5, column = 6)
Rock.grid(row=6, column=5)
Paper.grid(row=7, column=5)
Scissors.grid(row=8, column=5)
Submit_button.grid(row=6, column=6)
Result.grid(row =10, column = 5)



main_window.mainloop()

                  
