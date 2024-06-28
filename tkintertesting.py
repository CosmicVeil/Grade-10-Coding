import tkinter
from random import randint

def generate_number():
    random_number = randint(1,100)
    number_label.configure(text=f"Random Number: {random_number}")


main_window = tkinter.Tk()
main_window.title("Random number generator")

number_label = tkinter.Label(main_window, text="Click the button to generate a random number!", wraplength=350)

number_label.pack(pady=20)

button = tkinter.Button(main_window, text="Generate Number", command = generate_number, bg='light green', fg="black")

button.pack(pady=10)

main_window.mainloop()