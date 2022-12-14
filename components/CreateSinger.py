from tkinter import *
from tkinter import ttk, messagebox
from tkinter import IntVar

from components.ListItem import ListItem
from db.create_random_id import create_random_id
from db.Sqlite import insert_singer

class CreateSinger:
    def __init__(self, master):
        self.master = master
        lable = ttk.Label(master, text="ایجاد خواننده")
        lable.grid(row=0, column=1)

        lable_name = ttk.Label(master, text="نام خواننده")
        lable_name.grid(row=1, column=0)
        self.input_name = Text(master, width=30, height=2)
        self.input_name.grid(row=1, column=1)

        lable_style = ttk.Label(master, text="سبک خواننده")
        lable_style.grid(row=2, column=0)
        self.input_style = Text(master, width=30, height=2)
        self.input_style.grid(row=2, column=1)

        lable_age = ttk.Label(master, text="سن خواننده")
        lable_age.grid(row=3, column=0)
        self.input_age = Text(master, width=30, height=2)
        self.input_age.grid(row=3, column=1)

        self.gender = IntVar()
        lable_gender = ttk.Label(master, text="جنسیت ")
        lable_gender.grid(row=4, column=0)
        checkbox_gender_men = Radiobutton(master, text='مرد', variable=self.gender, value=1)
        checkbox_gender_women = Radiobutton(master, text='زن', variable=self.gender, value=0)
        checkbox_gender_men.grid(row=4, column=1)
        checkbox_gender_women.grid(row=4, column=2)

        ttk.Button(master, text="ثبت", command=self.insert_data).grid(row=5, column=0, columnspan=2)

    def insert_data(self):
        data = (create_random_id(), self.input_name.get("1.0", "end-1c"), self.input_style.get("1.0",
                "end-1c"), self.input_age.get("1.0", "end-1c"), self.gender.get())
        print(data)
        result = insert_singer(data)
        messagebox.showinfo("وضعیت", result)
        parent_name = self.master.winfo_parent()
        parent = self.master._nametowidget(parent_name)
        parent.destroy()


