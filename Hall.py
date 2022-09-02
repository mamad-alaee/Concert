from tkinter import *
from tkinter import ttk


class Hall:
    def __init__(self, master):
        self.lable = ttk.Label(master, text="Hall")
        self.lable.grid(row=4, column=0, columnspan=2)



