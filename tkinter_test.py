# import tkinter

# def main():
#     main_window = tkinter.Tk()
#     tkinter.mainloop()

# main()

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, 
                                   text='Mohan')
        self.label2 = tkinter.Label(self.top_frame, text='Dhruv')

        self.label3 = tkinter.Label(self.bottom_frame,text='Varun')
        self.label4 = tkinter.Label(self.bottom_frame,text='Evan')
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='left')
        self.label4.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

my_gui = MyGUI()