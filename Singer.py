from tkinter import *
from tkinter import ttk


class Singer:
    def __init__(self, master):
        self.lable = ttk.Label(master, text="singer")
        self.lable.grid(row=4, column=0, columnspan=2)



