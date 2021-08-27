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
        del_cust=Del_cust_Frame(self,controller)
        del_cust.place(x=250, y=150, height=500, width=600)

class Del_cust_Frame(tk.Frame):
    def onBackClick(self,controller):
        controller.show_frame("C")
    def onClickDelete(self,parent,text):
        conn=sqlite3.connect('bentley.db')
        if text=="P":
            c=conn.cursor()
            try:
                c.execute('''
                    delete  from customer where phno=?;
                ''',(self.phno.get()))
                eu = tk.Label(parent, text="DELETION DONE SUCCESSFULLY", font=("Arial", 10, "bold"), bg="#FFFDD0",
                              fg="black")
                eu.place(x=300, y=550)
            except:
                eu = tk.Label(parent, text="DELETION FAILED!!! PHONE NUMBER DOESNOT EXIST", font=("Arial", 10, "bold"), bg="#FFFDD0",
                              fg="black")
                eu.place(x=300, y=550)
        else:
            c=conn.cursor()
            try:
                c.execute('''
                    delete from customer where id=?;
                ''',(self.id.get()))
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
        if text=="PHONE NUMBER":
            a=tk.Label(parent,text="PHONE NUMBER: ",bg="#FFFDD0",font=("Arial",15,"bold"))
            a.place(x=300,y=350)
            self.phno=tk.Entry(parent,bg="#FFFDD0",font=("Arial",15,"bold"))
            self.phno.place(x=500,y=350)
            dlt_btn=tk.Button(parent,text="DELETE",font=("Helventica", 10, "bold"),command=lambda: self.onClickDelete(parent,"P"),fg="white",width=7,height=1,bg="blue")
            dlt_btn.place(x=300,y=400)
        else:
            a=tk.Label(parent,text="CUSTOMER ID: ",bg="#FFFDD0",font=("Arial",15,"bold"))
            a.place(x=300,y=350)
            self.id=tk.Entry(parent,bg="#FFFDD0",font=("Arial",15,"bold"))
            self.id.place(x=500,y=350)
            dlt_btn=tk.Button(parent,text="DELETE",font=("Helventica", 10, "bold"),command=lambda: self.onClickDelete(parent,"I"),fg="white",width=7,height=1,bg="blue")
            dlt_btn.place(x=300,y=400)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="DELETION", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=400,y=170)
        del_by=tk.Label(parent,text="DELETE BY :",font=("Arial",20,"bold"),bg="#FFFDD0",fg="black").place(x=310,y=260)
        clicked=StringVar()
        clicked.set("PHONE NUMBER")
        del_set_drop=tk.OptionMenu(parent,clicked,"ID","PHONE NUMBER")
        del_set_drop.place(x=500,y=262)
        prcd_btn=tk.Button(parent, text="PROCEED",fg="white",width=7,height=1,bg="brown",command=lambda: self.onProceedClick(parent,clicked.get()),font=("Helventica", 10, "bold"))
        prcd_btn.place(x=650,y=263)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(controller))
        back.place(x=270,y=600)
