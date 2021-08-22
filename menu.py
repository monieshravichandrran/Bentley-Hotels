import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        cust=MenuBars(self,controller,"Customer")
        cust.place(x=170,y=70,height=300,width=350)
        emp=MenuBars(self,controller,"Employee")
        emp.place(x=570,y=70,height=300,width=350)
        Bill=MenuBars(self,controller,"Bill")
        Bill.place(x=170,y=420,height=300,width=350)
        logout=MenuBars(self,controller,"Logout")
        logout.place(x=570,y=420,height=300,width=350)

class MenuBars(tk.Frame):
    def __init__(self,parent,controller,txt):
        tk.Frame.__init__(self,parent,bg="#FFFDD0",highlightbackground="black",highlightthickness=5)
        if txt=="Customer":
            B=tk.Button(parent,text=txt+"\nManagement",width=27,height=11,bg="#FFFDD0",font=("Helventica",15,"bold")).place(x=180,y=80)
        elif txt=="Employee":
            B=tk.Button(parent,text=txt+"\nManagement",width=27,height=11,bg="#FFFDD0",font=("Helventica",15,"bold")).place(x=580,y=80)
        elif txt=="Bill":
            B=tk.Button(parent,text=txt+"\nCalculator",width=27,height=11,bg="#FFFDD0",font=("Helventica",15,"bold")).place(x=180,y=430)
        else:
            B=tk.Button(parent,text=txt,width=27,height=11,bg="#FFFDD0",font=("Helventica",15,"bold")).place(x=580,y=430)
