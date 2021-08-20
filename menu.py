import tkinter as tk
from PIL import ImageTk

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        cust=MenuBars(self,controller)
        cust.place(x=150,y=50,height=300,width=350)
        emp=MenuBars(self,controller)
        emp.place(x=550,y=50,height=300,width=350)
        Bill=MenuBars(self,controller)
        Bill.place(x=150,y=400,height=300,width=350)
        logout=MenuBars(self,controller)
        logout.place(x=550,y=400,height=300,width=350)
