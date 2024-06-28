import customtkinter as ctk
import tkinter.messagebox as tkmb

def print_message():
    tkmb.showinfo("Result", "HEllo")


root = ctk.CTk()
root.geometry("400x500")

btn = ctk.CTkButton(root, text="Click", command=print_message, ).pack()

lbl = ctk.CTkLabel(root, text="Wsp").pack()

root.mainloop()