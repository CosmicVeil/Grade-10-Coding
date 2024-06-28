#Name: mohan
# Purpose: Tkinter

import tkinter as tk

main = tk.Tk()

main.geometry('1000x800')
main.configure(background='grey')

label1 = tk.Label(text="Math", fg="pink")
label2 = tk.Label(text="Comp Sci", fg="pink")
label3 = tk.Label(text="History", fg="pink")
label4 = tk.Label(text="Civics", fg="pink")

label1.grid(row=0,column=0, padx=0)
label2.grid(row=1,column=0,padx=0,pady=100)
label3.grid(row=2,column=0,padx=0, pady=100)
label4.grid(row=3,column=0,padx=0,pady=100)

main.mainloop()