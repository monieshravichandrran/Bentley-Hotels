from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3
class Upd_cust(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        upd=upd_cust_Fram(self,controller)
        upd.place(x=250,y=150,height=500,width=600)

class upd_cust_Fram(tk.Frame):
    def onBackClick(self,controller):
        controller.show_frame("C")
    def onContinueClick(self,parent,type,text,checker):
        conn=sqlite3.connect()
        if type=="PH":
            if text=="NAME":
                c=conn.cursor()
                x=tk.Label(parent,text="NAME: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=500,y=450)
                name_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                c.execute('''
                        update customer set Name=? where phone=?
                ''',name_i,checker)
            elif text=="AGE":
                c=conn.cursor()
                x=tk.Label(parent,text="AGE: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=500,y=450)
                age_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                c.execute('''
                        update customer set Name=? where phone=?
                ''',age_i,checker)
            else:
                c=conn.cursor()
                x=tk.Label(parent,text="MEMBERSHIP: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=500,y=450)
                member_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                c.execute('''
                       update customer set member=? where phone=?
                ''',member_i,checker)
        else:
            if text=="NAME":
                c=conn.cursor()
                x=tk.Label(parent,text="NAME: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=500,y=450)
                name_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                c.execute('''
                                update customer set Name=? where id=?
                          ''',name_i,checker)
            elif text=="AGE":
                c = conn.cursor()
                x = tk.Label(parent, text="AGE: ", font=("Arial", 15, "bold"), bg="#FFFDD0", fg="black").place(x=500,y=450)
                age_i = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
                c.execute('''
                                update customer set age=? where id=?
                          ''', age_i, checker)
            else:
                c = conn.cursor()
                x = tk.Label(parent, text="AGE: ", font=("Arial", 15, "bold"), bg="#FFFDD0", fg="black").place(x=500,y=450)
                member_i = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
                c.execute('''
                                update customer set age=? where id=?
                          ''', member_i, checker)
        conn.commit()
        conn.close()
    def onProceedClick(self,parent,text):
        if(text=="PHONE NUMBER"):
            tk.Label(parent,text="PHONE NUMBER: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=370)
            self.phno = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
            self.phno.place(x=480, y=370)
            clicked = StringVar()
            clicked.set("NAME")
            tk.Label(parent,text="UPDATE? ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=420)
            upd_drop = tk.OptionMenu(parent, clicked,"NAME", "AGE","MEMBERSHIP")
            upd_drop.place(x=410, y=420)
            self.cont=tk.Button(parent,text="Continue",command=lambda: self.onContinueClick(parent,"PH",clicked.get(),self.phno),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="GREEN")
            self.cont.place(x=500,y=420)
        else:
            tk.Label(parent,text="CUSTOMER ID: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=370)
            self.id = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
            self.id.place(x=480, y=370)
            clicked = StringVar()
            clicked.set("NAME")
            tk.Label(parent,text="UPDATE? ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=420)
            upd_drop = tk.OptionMenu(parent, clicked,"NAME", "AGE","MEMBERSHIP")
            upd_drop.place(x=410, y=420)
            cont=tk.Button(parent,text="Continue",command=lambda: self.onContinueClick(parent,"ID",clicked.get(),self.id),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="GREEN")
            cont.place(x=540,y=420)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="UPDATION", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=400,y=170)
        upd_by=tk.Label(parent,text="UPDATE BY :",font=("Arial",20,"bold"),bg="#FFFDD0",fg="black").place(x=330,y=260)
        clicked=StringVar()
        clicked.set("ID")
        upd_set_drop=tk.OptionMenu(parent,clicked,"ID","PHONE NUMBER")
        upd_set_drop.place(x=500,y=262)
        prcd_btn=tk.Button(parent, text="PROCEED",fg="white",width=7,height=1,bg="brown",command=lambda: self.onProceedClick(parent,controller,clicked.get()),font=("Helventica", 10, "bold"))
        prcd_btn.place(x=330,y=315)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(controller))
        back.place(x=270,y=600)
