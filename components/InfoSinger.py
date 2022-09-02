from tkinter import *
from tkinter import ttk
from tkinter import IntVar



class InfoSinger:
    def __init__(self, master):
        self.lable = ttk.Label(master, text="ایجاد خواننده")
        self.lable.grid(row=0, column=1)

        self.lable_name = ttk.Label(master, text="نام خواننده")
        self.lable_name.grid(row=1, column=0)
        self.input_name = Text(master, width=30, height=2)
        self.input_name.grid(row=1, column=1)

        self.lable_style = ttk.Label(master, text="سبک خواننده")
        self.lable_style.grid(row=2, column=0)
        self.input_style = Text(master, width=30, height=2)
        self.input_style.grid(row=2, column=1)

        self.lable_age = ttk.Label(master, text="سن خواننده")
        self.lable_age.grid(row=3, column=0)
        self.input_age = Text(master, width=30, height=2)
        self.input_age.grid(row=3, column=1)

        self.gender = IntVar()
        self.lable_gender = ttk.Label(master, text="جنسیت ")
        self.lable_gender.grid(row=4, column=0)
        self.checkbox_gender_men = Radiobutton(master, text='مرد', variable=self.gender, value=1)
        self.checkbox_gender_women = Radiobutton(master, text='زن', variable=self.gender, value=0)
        self.checkbox_gender_men.grid(row=4, column=1)
        self.checkbox_gender_women.grid(row=4, column=2)

        ttk.Button(master, text="حذف").grid(row=5, column=0, columnspan=2)


