from tkinter import *
from tkinter import ttk, messagebox
from tkinter import IntVar

from db.Sqlite import delete_singer

class InfoSinger:
    def __init__(self, master, data):
        self.id = data[0]
        self.master = master

        lable = ttk.Label(master, text="ایجاد خواننده")
        lable.grid(row=0, column=1)

        lable_name = ttk.Label(master, text="نام خواننده")
        lable_name.grid(row=1, column=0)
        input_name = Text(master, width=30, height=2)
        input_name.grid(row=1, column=1)
        input_name.insert(INSERT, data[1])
        input_name['state'] = 'disabled'

        lable_style = ttk.Label(master, text="سبک خواننده")
        lable_style.grid(row=2, column=0)
        input_style = Text(master, width=30, height=2)
        input_style.grid(row=2, column=1)
        input_style.insert(INSERT, data[2])
        input_style['state'] = 'disabled'

        lable_age = ttk.Label(master, text="سن خواننده")
        lable_age.grid(row=3, column=0)
        input_age = Text(master, width=30, height=2)
        input_age.grid(row=3, column=1)
        input_age.insert(INSERT, data[3])
        input_age['state'] = 'disabled'

        lable_gender = ttk.Label(master, text="جنسیت خواننده")
        lable_gender.grid(row=4, column=0)
        input_gender = Text(master, width=30, height=2)
        input_gender.grid(row=4, column=1)
        if data[4] == 0:
            input_gender.insert(INSERT, "خانم")
        elif data[4] == 1:
            input_gender.insert(INSERT, "آقا")
        else:
            input_gender.insert(INSERT, "نا معتبر")
        input_gender['state'] = 'disabled'

        ttk.Button(master, text="حذف", command=self.removing_item).grid(row=5, column=0, columnspan=2)

    def removing_item(self):
        where_filter = f"WHERE id={self.id}"
        result = delete_singer(where_filter)

        messagebox.showinfo("وضعیت", result)
        parent_name = self.master.winfo_parent()
        parent = self.master._nametowidget(parent_name)
        parent.destroy()

