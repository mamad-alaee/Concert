from tkinter import *
from tkinter import ttk

from components.ListItem import ListItem
from db.Sqlite import read_singer

class Singer:
    def __init__(self, master):
        lable = ttk.Label(master, text="آرتیست ها")
        lable.grid(row=0, column=0, columnspan=1)

        singers = read_singer("")

        index = 2
        for data in singers:
            ListItem(master, data[1], data[2], index, "singer",data)
            index += 1
