#Names: Daniel, Dhruv, Varun, Jason
#Date: Apr 29
#Purpose: Nursery Rhyme GUI

import tkinter as tk
import tkinter.messagebox as tkmb

def main():
    main_window = tk.Tk()
    main_window.title("Nursery Rhymes")
    main_window.geometry("1500x500")

    QuestionFrame = tk.Frame(main_window)
    BFrame = tk.Frame(main_window)

    Question = tk.Label(QuestionFrame,
                        text = "Would you like to see some nursery rhymes?",
                        fg = "black", bg = "white", font = ("Georgia", 30))
    
    go_button = tk.Button(BFrame,text="Yes",fg="blue", bg="light green",
                          font=("Georgia", 20,"bold"),height=10,width=20,command=rhymes)
    no_button = tk.Button(BFrame,text="No",fg="red", bg="orange",
                          font=("Georgia",20,"bold"),height=10,width=20,command=main_window.destroy)

    Question.pack()
    QuestionFrame.pack()
    BFrame.pack()
    go_button.pack(side='left')
    no_button.pack(side='left')

def rhymes():
    rhyme_window = tk.Tk()
    rhyme_window.title("Nursery Rhymes")
    rhyme_window.geometry("500x500")
	
    top_frame = tk.Frame(rhyme_window)
    bottom_frame = tk.Frame(rhyme_window)

    menu = tk.Label(top_frame, text="1. Johnny Johnny Yes Papa\n2. You thought I was feelin you\n3. Curry La Curry",
                    font=("Georgia", 12), fg="pink", bg="blue")
    name_instruct = tk.Label(top_frame, text="Enter your name so our rhymes can be for you!")
    rhyme_prompt = tk.Label(bottom_frame, text="Which rhyme would you like to hear?")
    name_entry = tk.Entry(top_frame)
    entry = tk.Entry(bottom_frame)
    chosen_rhyme = entry.get()
    exit_button = tk.Button(bottom_frame, text="Exit", command=rhyme_window.destroy)
    
    def show_rhyme():
        name = name_entry.get()
        chosen_rhyme = entry.get()
        if chosen_rhyme == "1":
            tkmb.showinfo("Johnny, Johnny Yes Papa",""+name+" "+name+" yes papa.\nEating sugar no papa\nTelling lies no pa, pa.\nOpen your mouth."
                          "\nHa!\nHa!\nHa!")
        elif chosen_rhyme == "2":
            tkmb.showinfo("You thought I was feelin you", "You thought I was feeling "+name+"\nYou thought I was beating "+name+"\nYou thought I was"
                          " touching "+name+"\nYou shall be a munch\nEating a tasty brunch\nPlaying baseball with "+name)
        elif chosen_rhyme == "3":
            tkmb.showinfo("Curry La Curry", "Oh, "+name+".\nI love my Curry.\nYou make me happy when I am hungry.")
        else:
            tkmb.showinfo("Error", "Error 404: Show Valid Response")

    submit_button = tk.Button(bottom_frame, text="Submit", command=show_rhyme)

    top_frame.pack()
    bottom_frame.pack()
    menu.pack()
    rhyme_prompt.pack()
    entry.pack()
    submit_button.pack()
    exit_button.pack()
    name_instruct.pack()
    name_entry.pack()

    tk.mainloop()

main()