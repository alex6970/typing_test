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

        # Main Frame
        self.test_frame = ct.CTkFrame(self, corner_radius=10, fg_color='red', height=self.win_height, width=self.win_width )
        self.test_frame.pack(padx=20, pady=20)

        # Infos bar frame
        self.info_frame = ct.CTkFrame(self.test_frame, fg_color='grey', corner_radius=10, height=55, width=self.winfo_width())
        self.info_frame.pack()

        mistakes_label = ct.CTkLabel(self.info_frame, textvariable='Hello', font=("Verdana", 9), fg_color=("white", "grey"))
        mistakes_label.pack() ## TO FIX

        time_label = ct.CTkLabel(self.info_frame, textvariable='lALA', font=("Verdana", 9), fg_color=("white", "grey"))
        time_label.pack() ## TO FIX
        
        # Test frame
        self.main_info_frame = ct.CTkFrame(self.test_frame, fg_color='grey', corner_radius=10, height=250, width=self.winfo_width())
        self.main_info_frame.pack()

        # Buttons frame
        self.btns_frame = ct.CTkFrame(self.test_frame, fg_color='grey', corner_radius=10, height=50, width=self.winfo_width())
        self.btns_frame.pack()





def main():
    Main().mainloop() 

# Runs only if compiled as own script, not as module
if __name__ == '__main__':
    main()



# TODO :
# Continue GUI => 3 Frames + FIX FRAME GESTION


