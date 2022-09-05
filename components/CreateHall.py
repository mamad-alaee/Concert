from tkinter import *
from tkinter import ttk, messagebox
import uuid
from db.Sqlite import insert_hall
from db.create_random_id import create_random_id




class CreateHall:
    def __init__(self, master):
        self.master = master
        lable = ttk.Label(master, text="ایجاد سالن")
        lable.grid(row=0, column=1)

        lable_name = ttk.Label(master, text="نام سالن")
        lable_name.grid(row=1, column=0)
        self.input_name = Text(master, width=30, height=2)
        self.input_name.grid(row=1, column=1)

        lable_amount = ttk.Label(master, text="گنجایش")
        lable_amount.grid(row=2, column=0)
        self.input_amount = Text(master, width=30, height=2)
        self.input_amount.grid(row=2, column=1)

        lable_address = ttk.Label(master, text="آدرس")
        lable_address.grid(row=3, column=0)
        self.input_address = Text(master, width=30, height=2)
        self.input_address.grid(row=3, column=1)

        ttk.Button(master, text="ثبت", command=self.insert_data).grid(row=5, column=0, columnspan=2)

    def insert_data(self):
        data = (create_random_id(), self.input_name.get("1.0", "end-1c"), self.input_amount.get("1.0", "end-1c"), self.input_address.get("1.0", "end-1c"))
        print(data)
        result = insert_hall(data)
        messagebox.showinfo("وضعیت", result)
        parent_name = self.master.winfo_parent()
        parent = self.master._nametowidget(parent_name)
        parent.destroy()
