from tkinter import *
from tkinter import ttk

from components.ListItem import ListItem


class Hall:
    def __init__(self, master):
        self.lable = ttk.Label(master, text="سالن های نمایش")
        self.lable.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text="ایجاد").grid(row=0, column=4, columnspan=2)

        fake_data = [{"name": "رشت", "amount": "5000"}, {"name": "تهران", "amount": "1000"},
                     {"name": "لاهیجان", "amount": "4000"},
                     {"name": "انزلی", "amount": "4500"}]

        index = 1
        for data in fake_data:
            ListItem(master, data["name"], data["amount"] , index)
            index += 1
