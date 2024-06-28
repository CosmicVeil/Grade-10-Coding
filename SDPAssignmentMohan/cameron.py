#name: Cameron Chen
#date: 5/13/2024
#purpose: Budget planner and tracker


import tkinter as tk
import tkinter.messagebox


def fileMenu():
    pass


def saveFile():
    pass


def budget_plan():
    #create the window
    window=tk.Tk()
    window.title("Budget")
    window.geometry("400x400")


    #creating the menubar
    menubar=tk.Menu(window)
    window.config(menu=menubar)
    #create open, save, and exit options
    filemenu=tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Open", command=fileMenu)
    filemenu.add_command(label="Save", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=window.destroy)


    #Creating the frames and packing them
    frame1=tk.Frame(window,relief="ridge",borderwidth=5)
    frame2=tk.Frame(window)
    frame3=tk.Frame(window,relief="ridge",borderwidth=5)
    frame4=tk.Frame(window)
    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack()


    #Creating the prompt label
    labelA=tk.Label(frame1,text="Your weekly budget",
                    fg="white",bg="black",font=("Garamond",15))



def budget_tracking(main, cbVar1, cbVar2, cbVar3, cbVar4, cbVar5, cbVar6, cbVar7, cbVar8):
        #create the window
        print(cbVar1.get())
        print(1)
        window=tk.Toplevel(main)
        window.title("Expense tracking part(2/2)")
        window.geometry("400x400")

        #creating the menubar
        menubar=tk.Menu(window)
        window.config(menu=menubar)
        #create open, save, and exit options
        filemenu=tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File",menu=filemenu)
        filemenu.add_command(label="Open", command=fileMenu)
        filemenu.add_command(label="Save", command=saveFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=window.destroy)


        #creating the necaessary frames and packing them
        frame1=tk.Frame(window,relief="ridge", borderwidth=5)
        frame2=tk.Frame(window)
        frame3=tk.Frame(window)
        frame1.pack()
        frame2.pack()
        frame3.pack()
   




        #Creating the prompt label
        labelA=tk.Label(frame1,text="Enter a value for the expenses:",
                       fg="white",bg="black",font=("Garamond",15))
       
        #Adding an entry value for every checkbox the user has clicked
        selected_expenses=""
        if cbVar1.get()==1:
            selected_expenses += "Housing\n"


        if cbVar2.get()==1:
            selected_expenses += "Personal care\n"


        if cbVar3.get()==1:
            selected_expenses += "Food\n"
           
        if cbVar4.get()==1:
            selected_expenses += "Transportation\n"


        if cbVar5.get()==1:
            selected_expenses += "Education\n"


        if cbVar6.get()==1:
            selected_expenses += "Miscellaneous\n"
           
        if cbVar7.get()==1:
            selected_expenses += "Healthcare\n"


        if cbVar8.get()==1:
            selected_expenses += "Debt payments\n"


        #Create labels for the user inputs and use for range to create entry values
        labelB=tk.Label(frame2,text=selected_expenses)
       


        #next and quit buttons
        next_button=tk.Button(frame3,text="next",command=lambda: budget_tracking(window, cbVar1, cbVar2, cbVar3, cbVar4, cbVar5, cbVar6, cbVar7, cbVar8),
                              fg="white",bg="green")
        quit_button=tk.Button(frame3,text="quit",command=window.destroy,
                              fg="white",bg="red")


        #packing all the widges in this function
        labelA.pack()
        labelB.pack()
        next_button.pack(side="left",padx=5)
        quit_button.pack(side="left")


        window.mainloop()



def expense(main):
    #Creating expense value tracker
    cbVar1=tk.IntVar()
    cbVar2=tk.IntVar()
    cbVar3=tk.IntVar()
    cbVar4=tk.IntVar()
    cbVar5=tk.IntVar()
    cbVar6=tk.IntVar()
    cbVar7=tk.IntVar()
    cbVar8=tk.IntVar()
   

    #create the window
    window=tk.Toplevel(main)
    window.title("Expense tracking part(1/2)")
    window.geometry("400x400")


    #creating the menubar
    menubar=tk.Menu(window)
    window.config(menu=menubar)
    #create open, save, and exit options
    filemenu=tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Open", command=fileMenu)
    filemenu.add_command(label="Save", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=window.destroy)


    #Creating the necessary frames and packing them and seperating them
    frame1=tk.Frame(window,relief="ridge", borderwidth=5)
    frame2=tk.Frame(window)
    frame3=tk.Frame(window)
    frame1.pack(padx=5,pady=5)
    frame2.pack(padx=5,pady=5)
    frame3.pack(padx=5,pady=5)


    #Creating the label
    label=tk.Label(frame1,text="Select all expenses that apply:",
                   fg="white",bg="black",font=("Garamond",15))


   


    tk.Checkbutton(frame2,text="Housing",variable=cbVar1, onvalue=1).pack()
    tk.Checkbutton(frame2,text="Personal care",variable=cbVar2, onvalue=1).pack()
    tk.Checkbutton(frame2,text="Food",variable=cbVar3, onvalue=1).pack()
    tk.Checkbutton(frame2,text="Transportation",variable=cbVar4, onvalue=1).pack()
    tk.Checkbutton(frame2,text="Education",variable=cbVar5, onvalue=1).pack()
    tk.Checkbutton(frame2,text="Miscellaneous",variable=cbVar6, onvalue=1).pack()
    tk.Checkbutton(frame2,text="Healthcare",variable=cbVar7, onvalue=1).pack()
    tk.Checkbutton(frame2,text="Debt payments",variable=cbVar8, onvalue=1).pack()



    #Next and quir button creation
    next_button=tk.Button(frame3,text="next",command= lambda: budget_tracking(window, cbVar1, cbVar2, cbVar3, cbVar4, cbVar5, cbVar6, cbVar7, cbVar8),
                          fg="white",bg="green")
    quit_button=tk.Button(frame3,text="quit",command=window.destroy,
                          fg="white",bg="red")


    #packing all the widgets
    label.pack()
    # cb1.pack()
    # cb2.pack()
    # cb3.pack()
    # cb4.pack()
    # cb5.pack()
    # cb6.pack()
    # cb7.pack()
    # cb8.pack()
    next_button.pack(side="left",padx=5)
    quit_button.pack(side="left")


    window.mainloop()






def income(): #Creating first GUI for income
    #Create the window and set size and title
    window=tk.Tk()
    window.title("Income Tracking")
    window.geometry("500x300")


    #creating the menubar
    menubar=tk.Menu(window)
    window.config(menu=menubar)
    #create open, save, and exit options
    filemenu=tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Open", command=fileMenu)
    filemenu.add_command(label="Save", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=window.destroy)


    #Creating the necessary frames and packing them and seperating them
    frame1=tk.Frame(window,relief="ridge", borderwidth=5)
    frame2=tk.Frame(window)
    frame3=tk.Frame(window,relief="ridge", borderwidth=5)
    frame4=tk.Frame(window)
    frame5=tk.Frame(window)
    frame1.pack(padx=5,pady=5)
    frame2.pack(padx=5,pady=5)
    frame3.pack(padx=5,pady=5)
    frame4.pack(padx=5,pady=5)
    frame5.pack(padx=5,pady=5)


    #1st label
    label1=tk.Label(frame1,text="What is your most reliable/biggest source of income:",
                    fg="white",bg="black",font=("Garamond",15))


    #radio buttons for users income  
    radioVar=tk.IntVar()
    radioVar.set(1)


    rb1=tk.Radiobutton(frame2,text="Job",variable=radioVar,value=1)
    rb2=tk.Radiobutton(frame2,text="Side Hustle",variable=radioVar,value=2)
    rb3=tk.Radiobutton(frame2,text="Allowance",variable=radioVar,value=3)
    rb4=tk.Radiobutton(frame2,text="No Source",variable=radioVar,value=4)


    #2nd label
    label2=tk.Label(frame3,text="On estimate, how much do you make a week:",
                    fg="white",bg="black",font=("Garamond",15))


    #Create entry box
    income_entry=tk.Entry(frame4)


    #next and quit buttons
    next_button=tk.Button(frame5,text="next",command=lambda: expense(window),
                          fg="white",bg="green")
    quit_button=tk.Button(frame5,text="quit",command=window.destroy,
                          fg="white",bg="red")


    #packing everything
    label1.pack()
    rb1.pack()
    rb2.pack()
    rb3.pack()
    rb4.pack()
    label2.pack()
    income_entry.pack()
    next_button.pack(side="left",padx=5)
    quit_button.pack(side="left")


    window.mainloop()
income()



