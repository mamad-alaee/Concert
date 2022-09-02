from tkinter import *
from tkinter import ttk
from tkinter import StringVar

from components.ListItem import ListItem


class CreateConcert:
    def __init__(self, master):
        self.lable = ttk.Label(master, text="ایجاد کنسرت")
        self.lable.grid(row=0, column=1)

        self.lable_singer_name = ttk.Label(master, text="انتخاب خواننده")
        self.lable_singer_name.grid(row=1, column=0)
        self.selected_singer = StringVar()
        self.combo_singer = ttk.Combobox(master, textvariable=self.selected_singer)
        self.combo_singer['values'] =("امیرعباس گلاب", "تهم", "مهراد هیدن", "شهرام صولتی")
        self.combo_singer['state'] = 'readonly'
        self.combo_singer.grid(row=1, column=1)

        self.lable_hall_name = ttk.Label(master, text="انتخاب سالن")
        self.lable_hall_name.grid(row=2, column=0)
        self.selected_hall = StringVar()
        self.combo_hall = ttk.Combobox(master, textvariable=self.selected_hall)
        self.combo_hall['values'] = ("رشت", "لاهیجان", "انزلی", "تهران")
        self.combo_hall['state'] = 'readonly'
        self.combo_hall.grid(row=2, column=1)

        self.lable_price = ttk.Label(master, text="قیمت")
        self.lable_price.grid(row=3, column=0)
        self.input_price = Text(master, width=30, height=2)
        self.input_price.grid(row=3, column=1)

        self.lable_date = ttk.Label(master, text="تاریخ")
        self.lable_date.grid(row=4, column=0)
        self.input_date = Text(master, width=30, height=2)
        self.input_date.grid(row=4, column=1)

        self.lable_start_time = ttk.Label(master, text="ساعت شروع")
        self.lable_start_time.grid(row=5, column=0)
        self.input_start_time = Text(master, width=30, height=2)
        self.input_start_time.grid(row=5, column=1)

        self.lable_end_time = ttk.Label(master, text="ساعت پایان")
        self.lable_end_time.grid(row=6, column=0)
        self.input_end_time = Text(master, width=30, height=2)
        self.input_end_time.grid(row=6, column=1)

        ttk.Button(master, text="ثبت").grid(row=7, column=0, columnspan=2)




