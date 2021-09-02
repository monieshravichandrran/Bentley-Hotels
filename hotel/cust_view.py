'''
VIEW CUSTOMER PAGE
'''
from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3

class View_cust(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.view=View_cust_Fram(self,controller)
        self.view.place(x=250,y=150,height=500,width=600)
    def reset(self,controller):
        del self.view
        self.view=View_cust_Fram(self,controller)
        self.view.place(x=250,y=150,height=500,width=600)

class View_cust_Fram(tk.Frame):
    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("C")
    def onViewClick(self,parent,checker):
        self.view_btn['state']=DISABLED
        conn=sqlite3.connect('bentley.db')
        c=conn.cursor()
        c.execute('select * from customer where phone=?;',(checker,))
        l=c.fetchall()
        if(len(l)==0):
            eu=tk.Label(parent,text="SPECIFIED PHONE NUMBER DOESNOT EXIST",bg="#FFFDD0",fg="black",font=("Arial",17,"bold"))
            eu.place(x=270,y=500)
        else:
            id=l[0][0]
            name=l[0][1]
            age=l[0][2]
            mem=l[0][3]
            member=StringVar()
            if mem=='V':
                member.set("VIP")
            elif mem=='S':
                member.set("SUPREME")
            else:
                member.set("PRIME")
            tk.Label(parent,text="Customer ID: "+str(id),bg="#FFFDD0",fg="black",font=("Arial",17,"bold")).place(x=300,y=330)
            tk.Label(parent,text="Name: "+name,bg="#FFFDD0",fg="black",font=("Arial",17,"bold")).place(x=300,y=380)
            tk.Label(parent,text="Age: "+str(age),bg="#FFFDD0",fg="black",font=("Arial",17,"bold")).place(x=300,y=430)
            tk.Label(parent,text="Member: "+member.get(),bg="#FFFDD0",fg="black",font=("Arial",17,"bold")).place(x=300,y=480)

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="VIEW CUSTOMER", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=390,y=170)
        phno_d=tk.Label(parent,text="PHONE: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        phno_d.place(x=330,y=260)
        self.phno=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.phno.place(x=460,y=265)
        self.view_btn=tk.Button(parent, text="VIEW",fg="white",width=10,height=1,bg="blue",font=("Helventica", 15, "bold"),
                               command=lambda: self.onViewClick(parent,self.phno.get()))
        self.view_btn.place(x=330,y=580)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=270,y=600)