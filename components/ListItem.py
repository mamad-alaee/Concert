from tkinter import *
from tkinter import ttk


class ListItem:
    def __init__(self, master, main_text , sub_text , index):
        self.lable = ttk.Label(master, text=main_text)
        self.lable.grid(row=index, column=0, columnspan=2)

        self.lable = ttk.Label(master, text=sub_text)
        self.lable.grid(row=index, column=2, columnspan=2)

        ttk.Button(master, text="بیشتر").grid(row=index, column=4)



