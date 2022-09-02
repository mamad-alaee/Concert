from tkinter import *
from tkinter import ttk
from tkinter import Toplevel

from components.InfoHall import InfoHall
from components.InfoConcert import InfoConcert
from components.InfoSinger import InfoSinger


class ListItem:
    def __init__(self, master, main_text , sub_text , index, mainComponent):
        parent_name = master.winfo_parent()
        self.parent = master._nametowidget(parent_name)
        self.state = mainComponent

        self.lable = ttk.Label(master, text=main_text)
        self.lable.grid(row=index, column=0, columnspan=2)

        self.lable = ttk.Label(master, text=sub_text)
        self.lable.grid(row=index, column=2, columnspan=2)

        ttk.Button(master, text="بیشتر", command=self.switching_to_info).grid(row=index, column=4)

    def switching_to_info(self):
        create_windows = Toplevel(self.parent)
        create_windows.geometry("350x280")
        create_windows.title("New Window")
        main_info_frame = ttk.Labelframe(create_windows, text="menu")
        main_info_frame.grid(row=0, column=0)
        if self.state == "hall":
            print("hello")
            main_create_frame = InfoHall(main_info_frame)
        elif self.state == "concert":
            main_create_frame = InfoConcert(main_info_frame)
        elif self.state == "singer":
            main_create_frame = InfoSinger(main_info_frame)






