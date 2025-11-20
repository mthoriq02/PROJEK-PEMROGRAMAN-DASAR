from customtkinter import *

class Format:
    def __init__(self, master):
        self.master = master
        master.title("AYo")
        master.geometry("320x580+500+50")

root = CTk()
Format(root)
root.mainloop()