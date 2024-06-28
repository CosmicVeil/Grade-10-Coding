#name: Cameron Chen
#date: 6/6/2024
#purpose: Lamentis-1 escape room FSP

#importing modules
import tkinter as tk 
import time
from PIL import Image, ImageTk
#from FSP_problem_1 import problem_1
#from FSP_problem_1 import binary_numbers


#intro_bg=Image.open("rocket.png")

    

def fileLetters():
    pass




#Story window after the introduction window 
def story(window):
    #destroy previous window 
    window.withdraw()
    #Creating the window 
    window1=tk.Toplevel()
    window1.title("Story")
    window1.geometry("600x600")
    window1.configure(bg="#AA9371")
    
    
    #Menubar creation 
    menubar=tk.Menu(window1)
    window1.config(menu=menubar)

    helpmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="binary numbers", command=binary_numbers)
    helpmenu.add_command(label="binary letters", command=fileLetters)


    #Creating the frames
    frame1=tk.Frame(window1)
    frame1.pack()


    #Background image
    intro_bg_tk = ImageTk.PhotoImage(intro_bg)
    label_bg = tk.Label(frame1, image=intro_bg_tk)


    #Crating the story introduction
    story_text = """You wake up on the moon and you find yourself on the moon next to a rocket. 
Loki and Sylvie are the two companions that you find who tell you they have been stuck on the moon for 5 years and have been trying to escape.
They tell you there is an evil alien named Arvind Kugenasan who is trying to keep you on the moon so you suffocate from his stinkiness.
Arvind Kuganesan only speaks in binary code. Your goal is to try and escape the moon with Loki and Sylvie. If you need to refer back to the hint windows
click the "Help" button"""
    story_label = tk.Label(frame1, text=story_text, bg="#AA9371",wraplength=600)


    #creating the next and quit button 
    next_button=tk.Button(frame1,text="next",font=25,
                           bg="#2DFE54",fg="black",
                           height=2,width=7,
                           command=lambda:problem_1(window1))

    
    quit_button=tk.Button(frame1,text="quit",font=25,
                          bg="#FF474C",fg="black",
                          height=2,width=7,
                          command=window1.destroy)


    #packing everything
    story_label.place(x=0,y=50)
    label_bg.pack()
    next_button.place(x=215, y=550)
    quit_button.place(x=320, y=550)


    #enter mainloop
    window.mainloop()







#Introduction window 
def introduction():
    #Creating the window 
    window=tk.Tk()
    window.title("Escaping The Destruction of Lamentis-1")
    window.geometry("600x600")
    window.configure(bg="#AA9371")
    
    
    #Menubar creation 
    menubar=tk.Menu(window)
    window.config(menu=menubar)

    helpmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="binary numbers", command=binary_numbers)
    helpmenu.add_command(label="binary letters", command=fileLetters)
    
    
    #Creating frames 
    frame1=tk.Frame(window)
    frame1.pack()
    

    #Background image 
    intro_bg_tk = ImageTk.PhotoImage(intro_bg)
    label = tk.Label(frame1, image=intro_bg_tk)
    

    #Title label
    def typewriter_animation(text, label, index=0):
        if index < len(text):
           label.  config(text=text[:index + 1])
           label.after(100, typewriter_animation, text, label, index + 1)
       
    
    title_label=tk.Label(frame1,text="",
                         font=("Comic Sans",15),bg="#AA9371",
                         relief="ridge",borderwidth=5)


    typewriter_animation("Escaping The Destruction of Lamentis-1",title_label)
    

    #Start and quit button 
    start_button=tk.Button(frame1,text="start",font=25,
                           bg="#2DFE54",fg="black",
                           height=2,width=7,
                           command=lambda: story(window))
    quit_button=tk.Button(frame1,text="quit",font=25,
                          bg="#FF474C",fg="black",
                          height=2,width=7,
                          command=window.destroy)
    
    
    #packing all the widgets 
    title_label.place(x=120, y=5)
    label.pack()
    start_button.place(x=215, y=550)
    quit_button.place(x=320, y=550)
    

    #main loop the window 
    window.mainloop()
    

#calling the function
introduction()





