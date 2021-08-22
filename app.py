import tkinter as tk
from login import Login
from menu import Menu
from customer import Customer
from bill import Bill
from hotel import Hotel

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
        frame_list=[Login,Menu,Customer,Bill,Hotel]
        for F in (frame_list):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = App()
app.mainloop()
