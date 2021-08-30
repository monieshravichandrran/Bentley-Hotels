import sqlite3
from tkinter import *
import tkinter as tk
from PIL import ImageTk

class Del_cust(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.del_cust=Del_cust_Frame(self,controller)
        self.del_cust.place(x=250, y=150, height=500, width=600)
    def reset(self,controller):
        del self.del_cust
        self.del_cust=Del_cust_Frame(self,controller)
        self.del_cust.place(x=250, y=150, height=500, width=600)

class Del_cust_Frame(tk.Frame):
    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("C")
    def onClickDelete(self,parent,text,checker):
        self.dlt_btn['state']=DISABLED
        conn=sqlite3.connect('bentley.db')
        if text=="P":
            ch=conn.cursor()
            ch.execute('select phone from customer;')
            rs1=ch.fetchall()
            rs=list()
            for i in rs1:
                rs.append(i[0])
            if checker not in rs:
                self.eu = tk.Label(parent, text="SPECIFIED PHONE NUMBER DOESNOT EXIST",font=("Arial", 10, "bold"), bg="#FFFDD0", fg="black")
                self.eu.place(x=300, y=540)
                return
            c=conn.cursor()
            try:
                c.execute('''
                    delete  from customer where phone=?;
                ''',(checker,))
                eu = tk.Label(parent, text="DELETION DONE SUCCESSFULLY", font=("Arial", 10, "bold"), bg="#FFFDD0",
                              fg="black")
                eu.place(x=300, y=550)
            except:
                eu = tk.Label(parent, text="DELETION FAILED!!! PHONE NUMBER DOESNOT EXIST", font=("Arial", 10, "bold"), bg="#FFFDD0",
                              fg="black")
                eu.place(x=300, y=550)
        else:
            ch=conn.cursor()
            ch.execute('select id from customer;')
            rs1=ch.fetchall()
            rs=list()
            for i in rs1:
                rs.append(i[0])
            if checker not in rs:
                self.eu = tk.Label(parent, text="SPECIFIED CUSTOMER ID DOESNOT EXIST",font=("Arial", 10, "bold"), bg="#FFFDD0", fg="black")
                self.eu.place(x=300, y=540)
                return
            c=conn.cursor()
            try:
                c.execute('''
                    delete from customer where id=?;
                ''',(checker,))
                eu = tk.Label(parent, text="DELETION DONE SUCCESSFULLY", font=("Arial", 10, "bold"), bg="#FFFDD0",
                              fg="black")
                eu.place(x=300, y=550)
            except:
                eu = tk.Label(parent, text="DELETION FAILED!!! CUSTOMER ID DOESNOT EXIST", font=("Arial", 10, "bold"), bg="#FFFDD0",
                              fg="black")
                eu.place(x=300, y=550)
        conn.commit()
        conn.close()
    def onProceedClick(self,parent,text):
        self.prcd_btn['state']=DISABLED
        if text=="PHONE NUMBER":
            a=tk.Label(parent,text="PHONE NUMBER: ",bg="#FFFDD0",font=("Arial",15,"bold"))
            a.place(x=300,y=350)
            self.phno=tk.Entry(parent,bg="#FFFDD0",font=("Arial",15,"bold"))
            self.phno.place(x=500,y=350)
            self.dlt_btn=tk.Button(parent,text="DELETE",font=("Helventica", 10, "bold"),command=lambda: self.onClickDelete(parent,"P",self.phno.get()),fg="white",width=7,height=1,bg="blue")
            self.dlt_btn.place(x=300,y=400)
        else:
            a=tk.Label(parent,text="CUSTOMER ID: ",bg="#FFFDD0",font=("Arial",15,"bold"))
            a.place(x=300,y=350)
            self.id=tk.Entry(parent,bg="#FFFDD0",font=("Arial",15,"bold"))
            self.id.place(x=500,y=350)
            self.dlt_btn=tk.Button(parent,text="DELETE",font=("Helventica", 10, "bold"),command=lambda: self.onClickDelete(parent,"I",int(self.id.get())),fg="white",width=7,height=1,bg="blue")
            self.dlt_btn.place(x=300,y=400)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="DELETION", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=400,y=170)
        del_by=tk.Label(parent,text="DELETE BY :",font=("Arial",20,"bold"),bg="#FFFDD0",fg="black").place(x=310,y=260)
        clicked=StringVar()
        clicked.set("PHONE NUMBER")
        del_set_drop=tk.OptionMenu(parent,clicked,"ID","PHONE NUMBER")
        del_set_drop.place(x=500,y=262)
        self.prcd_btn=tk.Button(parent, text="PROCEED",fg="white",width=7,height=1,bg="brown",command=lambda: self.onProceedClick(parent,clicked.get()),font=("Helventica", 10, "bold"))
        self.prcd_btn.place(x=650,y=263)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=270,y=600)
