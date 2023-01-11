#! .\tt_venv\scripts\python.exe
# line up is for code runner extension

from english_words import get_english_words_set
import tkinter as tk
from tkinter import messagebox
import customtkinter as ct
import random

# # Convert lib set type to a list containing all words
# english_dict = list(get_english_words_set(['web2'], lower=True))

# print(type(english_dict))
# print(english_dict[2])

# App GUI

class wind1:
    def __init__(self, root):
        self.root = root

        self.win_width = 600
        self.win_height = 400
        # self.frame = ct.CTkFrame(root)

        root.geometry("{}x{}+{}+{}".format(self.win_width, self.win_height, 500, 150))
        root.resizable(width=False, height=False)

        self.display_widgets()

    def display_widgets(self):
        self.label = ct.CTkLabel(self.root, text="This is our first GUI!")
        self.label.pack()

        self.close_button = ct.CTkButton(self.root, text="Close", command=self.root.quit)
        self.close_button.pack()

        

def main():
    root = ct.CTk()
    app = wind1(root)
    root.mainloop() 

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
# Center frame and go on with the rest of it (geters and seter to create each frame ?)


