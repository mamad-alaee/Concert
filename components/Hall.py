from tkinter import *
from tkinter import ttk

from components.ListItem import ListItem
from db.Sqlite import read_hall


class Hall:
    def __init__(self, master):
        self.lable = ttk.Label(master, text="سالن های نمایش")
        self.lable.grid(row=0, column=0, columnspan=2)

        halls = read_hall("")

        index = 1
        for data in halls:
            ListItem(master, data[1], data[2], index, "hall", data)
            index += 1
