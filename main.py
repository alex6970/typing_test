#! .\tt_venv\scripts\python.exe
# line up is for code runner extension

from english_words import get_english_words_set
from tkinter import *
from tkinter import messagebox
import customtkinter as ct
import random

# # Convert lib set type to a list containing all words
# english_dict = list(get_english_words_set(['web2'], lower=True))

# print(type(english_dict))
# print(english_dict[2])

# tkinter
# tkinter in OOP ?
class GUI_window:
    def __init__(self, master, inp_title):
        self.master = master
        master.title(inp_title)

        windowWidth = 500
        windowHeight = 200
        positionRight = int(master.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(master.winfo_screenheight()/2.5 - windowHeight/2)
        master.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))
        master.resizable(width=FALSE, height=FALSE)

        
        


        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = ct.CTkButton(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")


root = ct.CTk()
my_gui = GUI_window(root, "A GUI")
root.mainloop()