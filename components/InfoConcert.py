from tkinter import *
from tkinter import ttk
from tkinter import StringVar


class InfoConcert:
    def __init__(self, master, data):
        lable = ttk.Label(master, text="ایجاد کنسرت")
        lable.grid(row=0, column=1)

        print(data)

        lable_singer_name = ttk.Label(master, text="خواننده")
        lable_singer_name.grid(row=1, column=0)
        input_singer_name = Text(master, width=30, height=2)
        input_singer_name.grid(row=1, column=1)
        input_singer_name.insert(INSERT, data[8])
        input_singer_name['state'] = 'disabled'

        lable_hall_name = ttk.Label(master, text="سالن")
        lable_hall_name.grid(row=2, column=0)
        input_hall_name = Text(master, width=30, height=2)
        input_hall_name.grid(row=2, column=1)
        input_hall_name.insert(INSERT, data[13])
        input_hall_name['state'] = 'disabled'

        lable_price = ttk.Label(master, text="قیمت")
        lable_price.grid(row=3, column=0)
        input_price = Text(master, width=30, height=2)
        input_price.grid(row=3, column=1)
        input_price.insert(INSERT, data[1])
        input_price['state'] = 'disabled'

        lable_date = ttk.Label(master, text="تاریخ")
        lable_date.grid(row=4, column=0)
        input_date = Text(master, width=30, height=2)
        input_date.grid(row=4, column=1)
        input_date.insert(INSERT, data[2])
        input_date['state'] = 'disabled'

        lable_start_time = ttk.Label(master, text="ساعت شروع")
        lable_start_time.grid(row=5, column=0)
        input_start_time = Text(master, width=30, height=2)
        input_start_time.grid(row=5, column=1)
        input_start_time.insert(INSERT, data[3])
        input_start_time['state'] = 'disabled'

        lable_end_time = ttk.Label(master, text="ساعت پایان")
        lable_end_time.grid(row=6, column=0)
        input_end_time = Text(master, width=30, height=2)
        input_end_time.grid(row=6, column=1)
        input_end_time.insert(INSERT, data[4])
        input_end_time['state'] = 'disabled'

        ttk.Button(master, text="خرید بلیط").grid(row=8, column=0, columnspan=2)
        ttk.Button(master, text="حذف").grid(row=7, column=0, columnspan=2)
