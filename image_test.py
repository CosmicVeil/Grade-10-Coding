import tkinter
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("1000x1000")
# Create a photoimage object of the image in the path
image1 = Image.open("0x0.webp")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
# Position image
label1.pack(anchor="center")
root.mainloop()