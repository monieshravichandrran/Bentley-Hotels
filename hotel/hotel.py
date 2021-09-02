'''
    HOTEL AUDIT MAINTANANCE PAGE
'''

from tkinter import *
import tkinter as tk
from PIL import ImageTk

class Hotel(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        ht_staff=Hotel_Fram(self,controller,"Staff")
        ht_staff.place(x=170, y=70, height=300, width=350)
        ht_food_bev=Hotel_Fram(self,controller,"Food & Beverage")
        ht_food_bev.place(x=570, y=70, height=300, width=350)
        ht_admin=Hotel_Fram(self,controller,"Package")
        ht_admin.place(x=170, y=420, height=300, width=350)
        ht_view=Hotel_Fram(self,controller,"View")
        ht_view.place(x=570, y=420, height=300, width=350)

class Hotel_Fram(tk.Frame):
    def htbackclick(self,controller):
        controller.show_frame("M")
    def onClickStaff(self,contoller):
        contoller.show_frame("S")
    def onClickRes(self,controller):
        controller.show_frame("R")
    def onClickPack(self,controller):
        controller.show_frame("P")
    def onClickView(self,controller):
        controller.show_frame("PT")
    def __init__(self,parent,controller,txt):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        if txt == "Staff":
            B = tk.Button(parent, text=txt + "\nManagement", width=27, height=11, bg="#FFFDD0",
                          font=("Helventica", 15, "bold"),command=lambda:self.onClickStaff(controller)).place(x=180, y=80)
        elif txt == "Food & Beverage":
            B = tk.Button(parent, text="Restaurant" + "\nManagement", width=27, height=11, bg="#FFFDD0",
                          font=("Helventica", 15, "bold"),command=lambda: self.onClickRes(controller)).place(x=580, y=80)
        elif txt == "Package":
            B = tk.Button(parent, text=txt + "\nManagement", width=27, height=11, bg="#FFFDD0",
                          font=("Helventica", 15, "bold"),command=lambda: self.onClickPack(controller)).place(x=180, y=430)
        elif txt=="View":
            B=tk.Button(parent, text=txt+"\nPackage\nTarrif", width=27, height=11, bg="#FFFDD0",
                        command=lambda: self.onClickView(controller),font=("Helventica", 15, "bold")).place(x=580,y=430)
        back = tk.Button(parent, text="BACK", fg="white", bg="red", width=8,height=2,
                             command=lambda: self.htbackclick(controller))
        back.place(x=100, y=750)
