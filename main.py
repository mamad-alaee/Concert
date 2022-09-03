from tkinter import *
from tkinter import ttk
from components.Singer import Singer
from components.Hall import Hall
from components.Concert import Concert
from components.CreateConcert import CreateConcert
from components.CreateSinger import CreateSinger
from components.CreateHall import CreateHall
from db.Sqlite import create_tables


class Main:
    main_component = None

    def __int__(self):
        create_tables()
        self.root = Tk()
        self.root.configure(width=1000, height=600)
        self.root.configure(bg="lightblue")

        self.menu_frame = ttk.Labelframe(self.root, text="menu")
        self.menu_frame.grid(row=0, column=0)

        ttk.Button(self.menu_frame, text="سالن", command=self.set_frame_to_hall).grid(row=0, column=0, columnspan=2)
        ttk.Button(self.menu_frame, text="کنسرت", command=self.set_frame_to_concert).grid(row=0, column=2, columnspan=2)
        ttk.Button(self.menu_frame, text="آرتیست", command=self.set_frame_to_singer).grid(row=0, column=4,
                                                                                          columnspan=2)

        self.main_frame = ttk.Labelframe(self.root, text="main_component")
        self.main_frame.grid(row=2, column=0)

        self.main_component = Hall(self.main_frame)
        ttk.Button(self.main_frame, text="ایجاد", command=self.create_new_windows).grid(row=0, column=4, columnspan=2)

        self.root.mainloop()

    def set_frame_to_concert(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        self.main_component = Concert(self.main_frame)
        ttk.Button(self.main_frame, text="ایجاد", command=self.create_new_windows).grid(row=0, column=4, columnspan=2)

    def set_frame_to_hall(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        self.main_component = Hall(self.main_frame)
        ttk.Button(self.main_frame, text="ایجاد", command=self.create_new_windows).grid(row=0, column=4, columnspan=2)

    def set_frame_to_singer(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        self.main_component = Singer(self.main_frame)
        ttk.Button(self.main_frame, text="ایجاد", command=self.create_new_windows).grid(row=0, column=4, columnspan=2)

    def create_new_windows(self):
        create_windows = Toplevel(self.root)
        create_windows.geometry("350x250")
        create_windows.title("New Window")
        main_create_frame = ttk.Labelframe(create_windows, text="menu")
        main_create_frame.grid(row=0, column=0)
        print(self.main_component.__class__)
        if isinstance(self.main_component, Hall):
            print("hello")
            main_create_frame = CreateHall(main_create_frame)
        elif isinstance(self.main_component, Concert):
            main_create_frame = CreateConcert(main_create_frame)
        elif isinstance(self.main_component, Singer):
            main_create_frame = CreateSinger(main_create_frame)


if __name__ == '__main__':
    main = Main()
    main.__int__()
