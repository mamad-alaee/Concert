from tkinter import *
from tkinter import ttk

from components.ListItem import ListItem
from db.Sqlite import read_concert


class SearchResultConcert:
    def __init__(self, master,concerts):
        lable = ttk.Label(master, text="کنسرت ها")
        lable.grid(row=0, column=0, columnspan=1)

        # concerts = read_concert("")
        print(concerts)

        index = 2
        for data in concerts:
            ListItem(master, data[8], data[13], index, "concert", data)
            index += 1
