import tkinter as tk
from tkinter import messagebox
import tkmacosx

def submit_choice():
    # Retrieve the choice using the variable associated with the radio buttons
    choice = transport_mode.get()
    # Show an information box with the selected transportation mode
    messagebox.showinfo("Choice Submitted", f"You have chosen {choice} as your mode of transportation.")

# Create the main window
root = tk.Tk()
root.title("Travel Booking Application")

# Set the geometry of the window
root.geometry("400x200")
root.configure(bg='light blue')  # Set a light grey background color

topFrame = tk.Frame(root, relief="sunken", bg="light blue")
bottomFrame = tk.Frame(root, relief="sunken", bg="light blue")


label = tk.Label(topFrame, text="Select which option you want to choose!", bg="light blue").pack()

# Create a variable to hold the transportation mode
transport_mode = tk.StringVar(value="Car")  # Default value

# Create radio buttons for transportation modes
tk.Radiobutton(bottomFrame, text="Car", variable=transport_mode, value="Car",
               font=("Arial", 12), bg='light blue').pack(anchor='center', pady=2)
tk.Radiobutton(bottomFrame, text="Train", variable=transport_mode, value="Train",
               font=("Arial", 12), bg='light blue').pack(anchor="center", pady=2)
tk.Radiobutton(bottomFrame, text="Plane", variable=transport_mode, value="Plane",
               font=("Arial", 12), bg='light blue').pack(anchor="center", pady=2)

topFrame.pack()
bottomFrame.pack()

# Create a submit button
submit_btn = tkmacosx.Button(bottomFrame, text="Submit", command=submit_choice,
                       font=("Arial", 12), bg='light blue', fg='red')
submit_btn.pack(pady=20)

# Start the event loop
root.mainloop()
