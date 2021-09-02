'''
View Restaurant Item Page
'''
from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3

class View_res(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.view=View_res_Fram(self,controller)
        self.view.place(x=250,y=150,height=500,width=600)
    def reset(self,controller):
        del self.view
        self.view=View_res_Fram(self,controller)
        self.view.place(x=250,y=150,height=500,width=600)

class View_res_Fram(tk.Frame):
    def onViewClick(self,parent,name):
        self.view_btn['state']=DISABLED
        conn=sqlite3.connect('bentley.db')
        c=conn.cursor()
        c.execute("select * from restaurant where name=?",(name,))
        l=c.fetchall()
        if(len(l)==0):
            eu=tk.Label(parent,text="SPECIFIED ITEM DOESNOT EXIST",bg="#FFFDD0",fg="black",font=("Arial",17,"bold"))
            eu.place(x=270,y=500)
        else:
            id=l[0][0]
            typ=l[0][2]
            price=l[0][3]
            types=StringVar()
            if typ=="F":
                types.set("FOOD")
            else:
                types.set("BEVERAGE")
            tk.Label(parent,text="Item ID: "+str(id),bg="#FFFDD0",fg="black",font=("Arial",17,"bold")).place(x=300,y=330)
            tk.Label(parent,text="Item Type: "+types.get(),bg="#FFFDD0",fg="black",font=("Arial",17,"bold")).place(x=300,y=380)
            tk.Label(parent,text="Item price: "+str(price),bg="#FFFDD0",fg="black",font=("Arial",17,"bold")).place(x=300,y=430)
    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("R")
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="VIEW ITEM", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=390,y=170)
        name_d=tk.Label(parent,text="NAME: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        name_d.place(x=330,y=260)
        self.name=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.name.place(x=460,y=265)
        self.view_btn=tk.Button(parent, text="VIEW",fg="white",width=10,height=1,bg="blue",font=("Helventica", 15, "bold"),
                               command=lambda: self.onViewClick(parent,self.name.get()))
        self.view_btn.place(x=330,y=580)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=270,y=600)