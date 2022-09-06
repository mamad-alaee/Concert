from tkinter import *
from tkinter import ttk
from components.Singer import Singer
from components.Hall import Hall
from components.Concert import Concert
from components.CreateConcert import CreateConcert
from components.CreateSinger import CreateSinger
from components.CreateHall import CreateHall
from components.SearchResultHall import SearchResultHall
from components.SearchResultConcert import SearchResultConcert
from components.SearchResultSinger import SearchResultSinger
from db.Sqlite import create_tables
from db.Sqlite import search_concert, read_hall, read_singer


class Main:
    main_component = None
    search_box = None

    def __int__(self):
        create_tables()
        self.root = Tk()
        self.root.configure(width=1000, height=600)
        self.root.configure(bg="lightblue")
        # self.root.bind("<FocusIn>", self.handle_focus)
        menu_frame = ttk.Labelframe(self.root, text="menu")
        menu_frame.grid(row=0, column=0)

        ttk.Button(menu_frame, text="سالن", command=self.set_frame_to_hall).grid(row=0, column=0, columnspan=2)
        ttk.Button(menu_frame, text="کنسرت", command=self.set_frame_to_concert).grid(row=0, column=2, columnspan=2)
        ttk.Button(menu_frame, text="آرتیست", command=self.set_frame_to_singer).grid(row=0, column=4,
                                                                                     columnspan=2)

        self.main_frame = ttk.Labelframe(self.root, text="main_component")
        self.main_frame.grid(row=2, column=0)

        self.main_component = Hall(self.main_frame)
        ttk.Button(self.main_frame, text="ایجاد", command=self.create_new_windows).grid(row=0, column=4, columnspan=1)
        ttk.Button(self.main_frame, text="تازه سازی", command=self.handle_focus).grid(row=0, column=2, columnspan=1)

        self.search_box = Text(self.main_frame, width=30, height=1)
        self.search_box.grid(row=1, column=0, columnspan=2)
        ttk.Button(self.main_frame, text="جستجو", command=self.handle_search).grid(row=1, column=2, columnspan=1)

        self.root.mainloop()

    def set_frame_to_concert(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        self.main_component = Concert(self.main_frame)
        ttk.Button(self.main_frame, text="ایجاد", command=self.create_new_windows).grid(row=0, column=4, columnspan=1)
        ttk.Button(self.main_frame, text="تازه سازی", command=self.handle_focus).grid(row=0, column=2, columnspan=1)
        self.search_box = Text(self.main_frame, width=30, height=1)
        self.search_box.grid(row=1, column=0, columnspan=2)
        ttk.Button(self.main_frame, text="جستجو", command=self.handle_search).grid(row=1, column=2, columnspan=1)

    def set_frame_to_hall(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        self.main_component = Hall(self.main_frame)
        ttk.Button(self.main_frame, text="ایجاد", command=self.create_new_windows).grid(row=0, column=4, columnspan=1)
        ttk.Button(self.main_frame, text="تازه سازی", command=self.handle_focus).grid(row=0, column=2, columnspan=1)
        self.search_box = Text(self.main_frame, width=30, height=1)
        self.search_box.grid(row=1, column=0, columnspan=2)
        ttk.Button(self.main_frame, text="جستجو", command=self.handle_search).grid(row=1, column=2, columnspan=1)

    def set_frame_to_singer(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        self.main_component = Singer(self.main_frame)
        ttk.Button(self.main_frame, text="ایجاد", command=self.create_new_windows).grid(row=0, column=4, columnspan=1)
        ttk.Button(self.main_frame, text="تازه سازی", command=self.handle_focus).grid(row=0, column=2, columnspan=1)
        self.search_box = Text(self.main_frame, width=30, height=1)
        self.search_box.grid(row=1, column=0, columnspan=2)
        ttk.Button(self.main_frame, text="جستجو", command=self.handle_search).grid(row=1, column=2, columnspan=1)

    def create_new_windows(self):
        create_windows = Toplevel(self.root)
        create_windows.geometry("350x250")
        create_windows.title("create Window")
        main_create_frame = ttk.Labelframe(create_windows, text="menu")
        main_create_frame.grid(row=0, column=0)
        print(self.main_component.__class__)
        if isinstance(self.main_component, Hall):
            print("hello")
            CreateHall(main_create_frame)
        elif isinstance(self.main_component, Concert):
            CreateConcert(main_create_frame)
        elif isinstance(self.main_component, Singer):
            CreateSinger(main_create_frame)

    def handle_focus(self):
        print("reload")
        if isinstance(self.main_component, Hall):
            self.set_frame_to_hall()
        elif isinstance(self.main_component, Concert):
            self.set_frame_to_concert()
        elif isinstance(self.main_component, Singer):
            self.set_frame_to_singer()

    def handle_search(self):
        search_text = self.search_box.get("1.0", "end-1c")
        print(search_text)
        if isinstance(self.main_component, Hall):
            result = read_hall(f" WHERE name LIKE '{search_text}%'")
            print("hall", result)
            self.create_new_windows_for_search(result)
        elif isinstance(self.main_component, Concert):
            result = search_concert(search_text)
            print("Concert", result)
            self.create_new_windows_for_search(result)
        elif isinstance(self.main_component, Singer):
            result = read_singer(f" WHERE name LIKE '{search_text}%'")
            print("singer", result)
            self.create_new_windows_for_search(result)

    def create_new_windows_for_search(self, data):
        create_windows = Toplevel(self.root)
        create_windows.geometry("350x250")
        create_windows.title("create Window")
        main_create_frame = ttk.Labelframe(create_windows, text="menu")
        main_create_frame.grid(row=0, column=0)
        print(self.main_component.__class__)
        if isinstance(self.main_component, Hall):
            SearchResultHall(main_create_frame, data)
        elif isinstance(self.main_component, Concert):
            SearchResultConcert(main_create_frame, data)
        elif isinstance(self.main_component, Singer):
            SearchResultSinger(main_create_frame, data)


if __name__ == '__main__':
    main = Main()
    main.__int__()
