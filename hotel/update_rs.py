'''
Update Restaurant item page
'''
from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3

class Upd_rs(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.upd=Upd_rs_Fram(self,controller)
        self.upd.place(x=250,y=150,height=500,width=600)
    def reset(self,controller):
        del self.upd
        self.upd=Upd_rs_Fram(self,controller)
        self.upd.place(x=250, y=150, height=500, width=600)

class Upd_rs_Fram(tk.Frame):
    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("R")
    def onClickUpdate(self,parent,checker,setter):
        self.upd_btn['state']=DISABLED
        conn=sqlite3.connect('bentley.db')
        c=conn.cursor()
        t=conn.cursor()
        t.execute('select name from restaurant;')
        l=t.fetchall()
        li=list()
        for i in l:
            li.append(i[0])
        if checker not in li:
            self.eu = tk.Label(parent, text="SPECIFIED ITEM NAME DOESNOT EXIST", font=("Arial", 10, "bold"),
                               bg="#FFFDD0", fg="black")
            self.eu.place(x=300, y=540)
            return
        try:
            c.execute('''
                update restaurant set price=? where name=?;
            ''',(setter,checker,))
            self.eu = tk.Label(parent, text="UPDATION SUCCESSFULL!!!", font=("Arial", 10, "bold"),
                               bg="#FFFDD0", fg="black")
            self.eu.place(x=300, y=540)
        except:
            self.eu = tk.Label(parent, text="SPECIFIED ITEM NAME DOESNOT EXIST", font=("Arial", 10, "bold"),
                               bg="#FFFDD0", fg="black")
            self.eu.place(x=300, y=540)
        conn.commit()
        conn.close()
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="UPDATION", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=400,y=170)
        name_d=tk.Label(parent,text="NAME: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        name_d.place(x=330,y=260)
        self.name_d=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.name_d.place(x=460,y=265)
        price_d=tk.Label(parent,text="Price",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        price_d.place(x=330,y=380)
        self.price_d=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.price_d.place(x=460,y=385)
        self.upd_btn=tk.Button(parent, text="UPDATE",fg="white",width=10,height=1,bg="blue",font=("Helventica", 15, "bold"),command=lambda: self.onClickUpdate(parent,self.name_d.get(),self.price_d.get()))
        self.upd_btn.place(x=330,y=480)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=270,y=600)
