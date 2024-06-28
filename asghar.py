from tkinter import *
from tkinter import messagebox
from tkinter import ttk

entries = []

def infoScreen():
    def create_schedule(master, days, times):
        global entries  # Ensure entries is treated as a global list
        
        schedule_frame = Frame(master)
        schedule_frame.grid(row=4, column=0, columnspan=2)
        
        for i, day in enumerate(days):
            Label(schedule_frame, text=day).grid(row=0, column=i+1)

        for i, time in enumerate(times):
            Label(schedule_frame, text=time).grid(row=i+1, column=0)

        # Use a list to store the Entry widgets
        entries = []
        for i in range(len(times)):
            entry_row = []
            for j in range(len(days)):
                entry = Label(schedule_frame, font= ("Comic Sans MS", 15))
                entry.grid(row=i+1, column=j+1)
                entry_row.append(entry)
            entries.append(entry_row)

        save_button = Button(schedule_frame, text="Save Schedule", height=1, width=13)
        save_button.grid(row=len(times)+2, columnspan=len(days)+1)

    def AddTask_Clicked():
        name = entTaskName.get()
        priority = int(sclPriority.get())
        input_val = monthchoosen.get()
        index = 0

        if input_val == "9am - 4pm":
            index=0
        elif input_val == "8am - 5pm":
            index=1
        elif input_val == "7am - 6pm":
            index=2
        elif input_val == "6am - 7pm":
            index=3
        elif input_val == "":
            messagebox.showinfo(title="Try Again", message="Please Select the times you are free")
            return

        
        # Assuming entries is a listbox or a similar widget
        if priority == 1:
            entries[4][index].config(text=name)  
        elif priority == 2:
            entries[3][index].config(text=name)
        elif priority == 3:
            entries[2][index].config(text=name)
        elif priority == 4:
            entries[1][index].config(text=name)
        elif priority == 5:
            entries[0][index].config(text=name)

        entTaskName.delete(0, END)


    def make_table():
        input_val = monthchoosen.get()
        if input_val == "9am - 4pm":
            windowinfo.geometry("1050x600")
            create_schedule(windowinfo, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                            ["9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm"])
        elif input_val == "8am - 5pm":
            windowinfo.geometry("1050x650")
            create_schedule(windowinfo, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                            ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"])
        elif input_val == "7am - 6pm":
            windowinfo.geometry("1050x700")
            create_schedule(windowinfo, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                            ["7am", "8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm"])
        elif input_val == "6am - 7pm":
            windowinfo.geometry("1050x750")
            create_schedule(windowinfo, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                            ["6am", "7am", "8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm"])
        elif input_val == "":
            messagebox.showinfo(title="Try Again", message="Please Select the times you are free")

    # Make window 
    windowinfo = Tk()
    windowinfo.title("Getting Info")
    windowinfo.geometry("700x300")
    
    titleframe = Frame(windowinfo)
    titleframe.grid(row=0, column=0, columnspan=2)

    lblInfo = Label(titleframe, text="Info", font=("Comic Sans MS", 45,"bold"), bg="#EFEFEF")
    lblInfo.grid(row=0, column=0, columnspan=3)

    lblTaskName = Label(windowinfo, text="Task Name", font=("Comic Sans MS", 15,"bold"), bg="#EFEFEF")
    lblTaskName.grid(row=1, column=0, pady=20, sticky="e")

    entTaskName = Entry(windowinfo, font=("Comic Sans MS", 15), bg="#EFEFEF")
    entTaskName.grid(row=1, column=1, sticky="w")

    lblPriority = Label(windowinfo, text="Priority", font=("Comic Sans MS", 15,"bold"), bg="#EFEFEF")
    lblPriority.grid(row=2, column=0, sticky="e")
                        
    v1 = DoubleVar() 
    sclPriority = Scale(windowinfo, variable=v1, from_=1, to=5, orient=HORIZONTAL) 
    sclPriority.grid(row=2, column=1, sticky="w") 

    lblFree = Label(windowinfo, text="Timings Free", font=("Comic Sans MS", 15,"bold"), bg="#EFEFEF")
    lblFree.grid(row=3, column=0, pady=20, sticky="e")

    n = StringVar() 
    monthchoosen = ttk.Combobox(windowinfo, width=10, textvariable=n, font= ("Comic Sans MS", 15)) 
    monthchoosen['values'] = ('9am - 4pm', '8am - 5pm', '7am - 6pm', '6am - 7pm') 
    monthchoosen.grid(row=3, column=1, sticky="w") 

    btnAdd = Button(windowinfo, text="Add Task", font=("Comic Sans MS", 15), height=1, width=13, relief="groove", command=AddTask_Clicked)
    btnAdd.grid(row=5, column=0, padx=30)

    btnOpen = Button(windowinfo, text="Open Schedule", font=("Comic Sans MS", 15), height=1, width=13, relief="groove", command=make_table)
    btnOpen.grid(row=5, column=1)

    # Configure resizing
    windowinfo.grid_rowconfigure(4, weight=1)
    windowinfo.grid_columnconfigure(0, weight=1)
    windowinfo.grid_columnconfigure(1, weight=1)

    windowinfo.mainloop()

infoScreen()