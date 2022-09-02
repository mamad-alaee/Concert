from tkinter import *
from tkinter import ttk
from components.Singer import Singer
from components.Hall import Hall
from components.Concert import Concert


class Main:
    main_component = None

    def __int__(self):
        self.root = Tk()
        self.menu_frame = ttk.Labelframe(self.root, text="menu")
        self.menu_frame.grid(row=0, column=0)

        ttk.Button(self.menu_frame, text="سالن", command=self.set_frame_to_hall).grid(row=0, column=0, columnspan=2)
        ttk.Button(self.menu_frame, text="کنسرت", command=self.set_frame_to_concert).grid(row=0, column=2, columnspan=2)
        ttk.Button(self.menu_frame, text="آرتیست", command=self.set_frame_to_singer).grid(row=0, column=4,
                                                                                          columnspan=2)

        self.main_frame = ttk.Labelframe(self.root, text="main_component")
        self.main_frame.grid(row=2, column=0)

        self.main_component = Hall(self.main_frame)

        self.root.mainloop()

    def set_frame_to_concert(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        self.main_component = Concert(self.main_frame)

    def set_frame_to_hall(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        self.main_component = Hall(self.main_frame)

    def set_frame_to_singer(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        self.main_component = Singer(self.main_frame)


if __name__ == '__main__':
    main = Main()
    main.__int__()
