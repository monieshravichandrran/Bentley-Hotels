from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3

class Upd_staff(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        upd=Upd_staff_Fram(self,controller)
        upd.place(x=250,y=150,height=500,width=600)

class Upd_staff_Fram(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="UPDATION", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=400,y=170)