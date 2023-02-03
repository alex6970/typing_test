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

        # # Main Frame
        # self.test_frame = ct.CTkFrame(self, corner_radius=10, fg_color='red')
        # self.test_frame.pack(padx=20, pady=20)
        

        # Infos bar frame
        self.info_frame = ct.CTkFrame(self, fg_color='grey',height=50, width=600)
        self.info_frame.pack(padx=20, pady=(20,2))
        self.info_frame.pack_propagate(0) # keep frame from shrinking to fit widget sizes

        time_label = ct.CTkLabel(self.info_frame, text='Time left :')
        time_label.pack(side=RIGHT, padx=(0,20)) 

        mistakes_label = ct.CTkLabel(self.info_frame, text='Mistakes :')
        mistakes_label.pack(side=LEFT, padx=(10,0)) 

        
        # Test frame
        self.main_info_frame = ct.CTkFrame(self, fg_color='grey',height=250, width=600)
        self.main_info_frame.pack(padx=20,pady=0)

        # Buttons frame
        self.btns_frame = ct.CTkFrame(self, fg_color='grey',height=50, width=600)
        self.btns_frame.pack(padx=20, pady=(2,20))





def main():
    Main().mainloop() 

# Runs only if compiled as own script, not as module
if __name__ == '__main__':
    main()



# TODO :
# Continue GUI => 3 Frames + FIX FRAME GESTION


