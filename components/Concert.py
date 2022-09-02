from tkinter import *
from tkinter import ttk

from components.ListItem import ListItem


class Concert:
    def __init__(self, master):
        self.lable = ttk.Label(master, text="کنسرت ها")
        self.lable.grid(row=0, column=0, columnspan=2)
        # ttk.Button(master, text="ایجاد").grid(row=0, column=4, columnspan=2)

        fake_data = [{"concert_hall": "تهران", "concert_singer": "علیرضا آذر"}, {"concert_hall": "تهران",
                                                                                 "concert_singer": "تتلو"},
                     {"concert_hall": "لاهیجان", "concert_singer": "مهراد هیدن"},
                     {"concert_hall": "انزلی", "concert_singer": "یاس"}]

        index = 1
        for data in fake_data:
            ListItem(master, data["concert_hall"], data["concert_singer"], index, "concert")
            index += 1
