#! .\tt_venv\scripts\python.exe
# line up is for code runner extension

from english_words import get_english_words_set
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import customtkinter as ct
import random

# # Convert lib set type to a list containing all words
# english_dict = list(get_english_words_set(['web2'], lower=True))

# print(type(english_dict))
# print(english_dict[2])

# App GUI
# Home page
class Main(ct.CTk):
    def __init__(self):
        super().__init__() # root is ct.CTK (arg)

        self.title("FastFingas.")

        self.win_width = 600
        self.win_height = 400

        self.geometry("{}x{}+{}+{}".format(self.win_width, self.win_height, 500, 150))
        self.resizable(width=False, height=False)

        self.home()


    def home(self):

        self.main_frame = ct.CTkFrame(self, bg_color='white', corner_radius=10)
        self.main_frame.pack()

        self.label = ct.CTkLabel(self.main_frame, text="This is our first GUI!")
        self.label.pack()

        self.new_window_button = ct.CTkButton(self.main_frame, text="Start", command=self.test)
        self.new_window_button.pack()

        self.close_button = ct.CTkButton(self.main_frame, text="Close", command=self.quit)
        self.close_button.pack()

    def test(self):
        self.main_frame.pack_forget()

        self.test_frame = ct.CTkFrame(self, bg_color='white', corner_radius=10, height=self.win_height-20, width=self.win_width-20 )
        self.test_frame.pack(padx=20, pady=20)






        
 
def main():
    Main().mainloop() 

# Runs only if compiled as own script, not as module
if __name__ == '__main__':
    main()



# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
#         self.button1.pack()
#         self.frame.pack()
#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Demo2(self.newWindow)

# TODO :
# Continue GUI


