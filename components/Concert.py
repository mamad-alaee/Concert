from tkinter import *
from tkinter import ttk

from components.ListItem import ListItem
from db.Sqlite import read_concert


class Concert:
    def __init__(self, master):
        lable = ttk.Label(master, text="کنسرت ها")
        lable.grid(row=0, column=0, columnspan=2)

        concerts = read_concert("")
        print(concerts)

        index = 1
        for data in concerts:
            ListItem(master, data[8], data[13], index, "concert", data)
            index += 1
