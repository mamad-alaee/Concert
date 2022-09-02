from tkinter import *
from tkinter import ttk


class Concert:
    def __init__(self, master):
        self.lable = ttk.Label(master, text="concert")
        self.lable.grid(row=4, column=0, columnspan=2)



