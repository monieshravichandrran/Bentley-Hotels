from tkinter import *
import tkinter as tk
from PIL import ImageTk

class Ins_cust(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        ins=Ins_cust_Fram(self,controller)
        ins.place(x=250,y=150,height=500,width=600)

class Ins_cust_Fram(tk.Frame):
    def onBackClick(self,controller):
        controller.show_frame("C")
    def oninsaClick(self,controller):
        controller.show_frame("CI")
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="INSERTION", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=400,y=170)
        name_d=tk.Label(parent,text="NAME: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        name_d.place(x=330,y=260)
        self.name=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.name.place(x=460,y=265)
        age_d=tk.Label(parent,text="AGE: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        age_d.place(x=330,y=320)
        self.age=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.age.place(x=460,y=325)
        phno_d=tk.Label(parent,text="PHONE: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        phno_d.place(x=330,y=380)
        self.phno=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.phno.place(x=460,y=385)
        ins_btn=tk.Button(parent, text="INSERT",fg="white",width=10,height=1,bg="blue",font=("Helventica", 15, "bold"))
        ins_btn.place(x=330,y=445)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(controller))
        back.place(x=270,y=600)
        ins_again=tk.Button(parent,text="INSERT AGAIN",bg="green",fg="white",command=lambda: self.oninsaClick(controller))
        ins_again.place(x=320,y=600)
