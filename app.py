import tkinter as tk
from tkinter import *
from login import Login
from menu import Menu
from customer import Customer
from bill import Bill
from hotel import Hotel
frame_name={"Lg":Login,"M":Menu,"C":Customer,"B":Bill,"H":Hotel}
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.title("Bentley Hotels")
        self.iconbitmap("images/logo.png")
        self.geometry("1219x800+100+0")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.frame_list=[Login,Menu,Customer,Bill,Hotel]
        for F in (self.frame_list):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Login)

    def show_frame(self, cont):
        global frame_name
        frame = self.frames[frame_name[cont]]
        frame.tkraise()

app = App()
app.mainloop()
