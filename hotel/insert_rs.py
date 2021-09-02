'''
Insert Restaurant item page
'''
from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3

class Ins_rs(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.ins = Ins_rs_Fram(self, controller)
        self.ins.place(x=250, y=150, height=500, width=600)
    def reset(self,controller):
        del self.ins
        self.ins=Ins_rs_Fram(self,controller)
        self.ins.place(x=250, y=150, height=500, width=600)

class Ins_rs_Fram(tk.Frame):
    def onClickInsert(self,parent,name,types,price):
        self.ins_btn['state']=DISABLED
        conn=sqlite3.connect('bentley.db')
        c=conn.cursor()
        t=conn.cursor()
        t.execute('SELECT max(id) FROM RESTAURANT;')
        l=t.fetchall()
        id=l[0][0]+1
        typess=StringVar()
        typess.set("N")
        if types=="FOOD":
            typess.set("F")
        elif types=="BEVERAGE":
            typess.set("B")
        try:
            c.execute('''
                    insert into restaurant values(?,?,?,?);
            ''',(int(id),name,typess.get(),price))
            eu = tk.Label(parent, text="INSERTION DONE SUCCESSFULLY", font=("Arial", 10, "bold"), bg="#FFFDD0",
                          fg="black")
            eu.place(x=300, y=550)
            conn.commit()
            conn.close()
        except:
            txt=StringVar()
            if len(name)==0:
                txt.set("INSERTION FAILED!!! ENTER NAME")
            elif int(price)==0:
                txt.set("INSERTION FAILED!!! ENTER PRICE")
            elif typess.get()=="N":
                txt.set("INSERTION FAILED!!! INVALID TYPE")
            else:
                txt.set("INSERTION FAILED!!!")
            eu = tk.Label(parent, text=txt.get(), font=("Arial", 10, "bold"), bg="#FFFDD0",
                          fg="black")
            eu.place(x=300, y=550)

    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("R")
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp = tk.Label(parent, text="INSERTION", bg="#FFFDD0", fg="#F99B03", font=("Helventica", 35, "bold"))
        disp.place(x=400, y=170)
        name_d=tk.Label(parent,text="NAME: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        name_d.place(x=330,y=260)
        self.name=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.name.place(x=460,y=265)
        types_d=tk.Label(parent,text="TYPE: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        types_d.place(x=330,y=320)
        self.types=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.types.place(x=460,y=325)
        price_d=tk.Label(parent,text="PRICE : ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        price_d.place(x=330,y=380)
        self.price=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.price.place(x=460,y=385)
        self.ins_btn=tk.Button(parent, text="INSERT",fg="white",width=10,height=1,bg="blue",font=("Helventica", 15, "bold"),
                               command=lambda: self.onClickInsert(parent,self.name.get(),self.types.get(),self.price.get()))
        self.ins_btn.place(x=330,y=480)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=270,y=600)
