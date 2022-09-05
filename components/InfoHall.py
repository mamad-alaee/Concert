from tkinter import *
from tkinter import ttk


class InfoHall:
    def __init__(self, master, data):
        print(data)
        lable = ttk.Label(master, text="ایجاد سالن")
        lable.grid(row=0, column=1)

        lable_name = ttk.Label(master, text="نام سالن")
        lable_name.grid(row=1, column=0)
        input_name = Text(master, width=30, height=2)
        input_name.grid(row=1, column=1)
        input_name.insert(INSERT, data[1])
        input_name['state'] = 'disabled'

        lable_amount = ttk.Label(master, text="گنجایش")
        lable_amount.grid(row=2, column=0)
        input_amount = Text(master, width=30, height=2)
        input_amount.grid(row=2, column=1)
        input_amount.insert(INSERT, data[2])
        input_amount['state'] = 'disabled'

        lable_address = ttk.Label(master, text="آدرس")
        lable_address.grid(row=3, column=0)
        input_address = Text(master, width=30, height=2)
        input_address.grid(row=3, column=1)
        input_address.insert(INSERT, data[3])
        input_address['state'] = 'disabled'

        ttk.Button(master, text="حذف").grid(row=5, column=0, columnspan=2)
