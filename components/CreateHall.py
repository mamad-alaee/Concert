from tkinter import *
from tkinter import ttk

from components.ListItem import ListItem


class CreateHall:
    def __init__(self, master):
        self.lable = ttk.Label(master, text="ایجاد سالن")
        self.lable.grid(row=0, column=1)

        self.lable_name = ttk.Label(master, text="نام سالن")
        self.lable_name.grid(row=1, column=0)
        self.input_name = Text(master, width=30, height=2)
        self.input_name.grid(row=1, column=1)

        self.lable_amount = ttk.Label(master, text="گنجایش")
        self.lable_amount.grid(row=2, column=0)
        self.input_amount = Text(master, width=30, height=2)
        self.input_amount.grid(row=2, column=1)

        self.lable_address = ttk.Label(master, text="آدرس")
        self.lable_address.grid(row=3, column=0)
        self.input_address = Text(master, width=30, height=2)
        self.input_address.grid(row=3, column=1)

        ttk.Button(master, text="ثبت").grid(row=5, column=0, columnspan=2)

