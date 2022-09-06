from tkinter import *
from tkinter import ttk

from components.ListItem import ListItem
from db.Sqlite import read_hall


class SearchResultHall:
    def __init__(self, master, halls):
        lable = ttk.Label(master, text="سالن های نمایش")
        lable.grid(row=0, column=0, columnspan=1)


        index = 2
        for data in halls:
            ListItem(master, data[1], data[2], index, "hall", data)
            index += 1
