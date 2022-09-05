from tkinter import *
from tkinter import ttk, messagebox
from tkinter import StringVar

from components.ListItem import ListItem
from db.create_random_id import create_random_id
from db.Sqlite import insert_concert
from db.Sqlite import get_ids_for_combobox


def getting_names_for_combo(ids):
    halls = ids[0]
    singers = ids[1]
    hall_names = []
    index = 0
    for hall in halls:
        print(hall[0])
        hall_names.insert(index, hall[0])
        index += 1
    singer_names = []
    index = 0
    for singer in singers:
        print(singer[0])
        singer_names.insert(index, singer[0])
        index += 1
    return singer_names, hall_names


def getting_id_of_selected_item(singer_name, hall_name, ids):
    halls = ids[0]
    singers = ids[1]
    hall_id = 0
    index = 0
    for hall in halls:
        if hall[0] == hall_name:
            hall_id = hall[1]
        index += 1
    singer_id = 0
    index = 0
    for singer in singers:
        if singer[0] == singer_name:
            singer_id = singer[1]
        index += 1
    return singer_id, hall_id


class CreateConcert:
    def __init__(self, master):
        self.master = master
        lable = ttk.Label(master, text="ایجاد کنسرت")
        lable.grid(row=0, column=1)
        self.ids = get_ids_for_combobox()
        names = getting_names_for_combo(self.ids)
        print(names[0])
        print(names[1])

        lable_singer_name = ttk.Label(master, text="انتخاب خواننده")
        lable_singer_name.grid(row=1, column=0)
        self.selected_singer = StringVar()
        combo_singer = ttk.Combobox(master, textvariable=self.selected_singer)
        combo_singer['values'] = names[0]
        combo_singer['state'] = 'readonly'
        combo_singer.grid(row=1, column=1)

        lable_hall_name = ttk.Label(master, text="انتخاب سالن")
        lable_hall_name.grid(row=2, column=0)
        self.selected_hall = StringVar()
        combo_hall = ttk.Combobox(master, textvariable=self.selected_hall)
        combo_hall['values'] = names[1]
        combo_hall['state'] = 'readonly'
        combo_hall.grid(row=2, column=1)

        self.lable_price = ttk.Label(master, text="قیمت")
        self.lable_price.grid(row=3, column=0)
        self.input_price = Text(master, width=30, height=2)
        self.input_price.grid(row=3, column=1)

        lable_date = ttk.Label(master, text="تاریخ")
        lable_date.grid(row=4, column=0)
        self.input_date = Text(master, width=30, height=2)
        self.input_date.grid(row=4, column=1)

        lable_start_time = ttk.Label(master, text="ساعت شروع")
        lable_start_time.grid(row=5, column=0)
        self.input_start_time = Text(master, width=30, height=2)
        self.input_start_time.grid(row=5, column=1)

        lable_end_time = ttk.Label(master, text="ساعت پایان")
        lable_end_time.grid(row=6, column=0)
        self.input_end_time = Text(master, width=30, height=2)
        self.input_end_time.grid(row=6, column=1)

        ttk.Button(master, text="ثبت", command=self.insert_data).grid(row=7, column=0, columnspan=2)

    def insert_data(self):
        ids = getting_id_of_selected_item(self.selected_singer.get(), self.selected_hall.get(), self.ids)
        data = (create_random_id(), self.input_price.get("1.0", "end-1c"), self.input_date.get("1.0", "end-1c"),
                self.input_start_time.get("1.0", "end-1c"), self.input_end_time.get("1.0", "end-1c"),
                ids[0], ids[1])
        # print(data)
        result = insert_concert(data)
        messagebox.showinfo("وضعیت", result)
        parent_name = self.master.winfo_parent()
        parent = self.master._nametowidget(parent_name)
        parent.destroy()
