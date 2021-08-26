from tkinter import *
import tkinter as tk
from PIL import ImageTk

class Upd_cust(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        disp=tk.Label(parent,text="UPDATE BASED ON: ").place(x=200,y=200,relwidth=1,relheight=1)
        
