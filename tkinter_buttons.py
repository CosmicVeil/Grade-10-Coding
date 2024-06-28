# Import the tkinter modules

import tkinter
import tkinter.messagebox
import tkmacosx

class ButtonGUI:
    def __init__(self):

        # Create the main window
        self.main_window = tkinter.Tk()

        # Set the label, title and background
        self.main_window.geometry("500x400")
        self.main_window.title("HW Check")
        self.main_window.config(bg="skyblue")

        # Create the top and bottom frame
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.top_frame.config(bg="skyblue")
        self.bottom_frame.config(bg="skyblue")

        # Create the label

        self.myLabel = tkinter.Label(self.top_frame, text="If you click the button below, I will give you a fun fact about me!", font=("Callibri", 15), bg="skyblue", fg="black")


        # Create the quit and fun fact buttons
        self.my_button = tkmacosx.Button(self.bottom_frame, text="Click Me!", fg="red", bg="black", command=self.do_something)
        self.quit_button = tkmacosx.Button(self.bottom_frame, text="Quit!",fg="red", bg="white", command=self.main_window.destroy)


        # Config the buttons
        self.my_button.config(height=100,width=100)
        self.quit_button.config(height=100,width=100)

        # Pack everything
        self.myLabel.pack(side="top", pady=(0,100))
        self.my_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack(anchor="n")
        self.bottom_frame.pack(anchor="s")

        tkinter.mainloop()

    # Function to give a fun fact
    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'A cloud weighs more than a million tons.')


my_gui = ButtonGUI()