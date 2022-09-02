from tkinter import *
from tkinter import ttk

from components.ListItem import ListItem


class Singer:
    def __init__(self, master):
        self.lable = ttk.Label(master, text="آرتیست ها")
        self.lable.grid(row=0, column=0, columnspan=2)
        ttk.Button(master, text="ایجاد").grid(row=0, column=4, columnspan=2)

        fake_data = [{"style": "پاپ", "name": "علیرضا آذر"}, {"style": "R&B",
                                                              "name": "تتلو"},
                     {"style": "رپ", "name": "مهراد هیدن"},
                     {"style": "رپ", "name": "یاس"}]

        index = 1
        for data in fake_data:
            ListItem(master, data["name"], data["style"], index)
            index += 1
