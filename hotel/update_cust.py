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
    def onClickUpdate(self,parent,text,type,checker,get_val):
        conn=sqlite3.connect('bentley.db')
        c=conn.cursor()
        c.execute('select phone from customer;')
        row=c.fetchall()
        if type=="P":
            if text=="N":
                try:
                    c=conn.cursor()
                    c.execute('''
                            update customer set Name=? where phone=?;
                    ''',(get_val,checker))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
                except:
                    self.eu=tk.Label(parent,text="SPECIFIED PHONE NUMBER DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
            elif text=="A":
                try:
                    c=conn.cursor()
                    c.execute('''
                        update customer set Name=? where phone=?;
                        ''',(get_val,checker))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300,y=540)
                except:
                    self.eu=tk.Label(parent,text="SPECIFIED PHONE NUMBER DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
            else:
                try:
                    c=conn.cursor()
                    c.execute('''
                        update customer set member=? where phone=?;
                    ''',(get_val,checker))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
                except:
                    self.eu=tk.Label(parent,text="SPECIFIED PHONE NUMBER DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
        else:
            if text=="N":
                try:
                    c=conn.cursor()
                    c.execute('''
                                update customer set Name=? where id=?;
                            ''',(get_val,checker))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
                except:
                    self.eu=tk.Label(parent,text="SPECIFIED CUSTOMER ID DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
            elif text=="A":
                try:
                    c=conn.cursor()
                    c.execute('''
                                    update customer set age=? where id=?;
                             ''', (get_val, checker))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
                except:
                    self.eu=tk.Label(parent,text="SPECIFIED CUSTOMER ID DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
            else:
                try:
                    c=conn.cursor()
                    c.execute('''
                                    update customer set member=? where id=?;
                              ''', (get_val, checker))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
                except:
                    self.eu=tk.Label(parent,text="SPECIFIED CUSTOMER DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
        conn.commit()
        conn.close()

    def onBackClick(self,parent,controller):
        self.__init__(parent,controller)
        controller.show_frame("C")
    def onContinueClick(self,parent,type,text,checker):
        if type=="PH":
            if text=="NAME":
                self.x=tk.Label(parent,text="NAME: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
                self.x.place(x=300,y=425)
                self.name_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                self.name_i.place(x=450,y=425)
                self.upd_btn=tk.Button(parent,text="UPDATE",font=("Helventica", 10, "bold"),command=lambda: self.onClickUpdate(parent,'N','P',self.name_i.get(),checker),fg="white",width=7,height=1,bg="blue")
                self.upd_btn.place(x=400,y=480)
            elif text=="AGE":
                self.x=tk.Label(parent,text="AGE: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
                self.x.place(x=300,y=425)
                self.age_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                self.age_i.place(x=450, y=425)
                self.upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'A','P',self.age_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                self.upd_btn.place(x=400,y=480)
            else:
                self.x=tk.Label(parent,text="MEMBERSHIP: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
                self.x.place(x=300,y=425)
                self.member_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                self.member_i.place(x=450, y=425)
                self.upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'M','P',self.member_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                self.upd_btn.place(x=400,y=480)
        else:
            if text=="NAME":
                self.x=tk.Label(parent,text="NAME: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
                self.x.place(x=300,y=425)
                self.name_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                self.name_i.place(x=450, y=425)
                self.upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'N','I',self.name_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                self.upd_btn.place(x=400,y=480)
            elif text=="AGE":
                self.x = tk.Label(parent, text="AGE: ", font=("Arial", 15, "bold"), bg="#FFFDD0", fg="black")
                self.x.place(x=300,y=450)
                self.age_i = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
                self.age_i.place(x=450, y=400)
                self.upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'A','I',self.age_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                self.upd_btn.place(x=400,y=480)
            else:
                self.x = tk.Label(parent, text="AGE: ", font=("Arial", 15, "bold"), bg="#FFFDD0", fg="black")
                self.x.place(x=300,y=450)
                self.member_i = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
                self.member_i.place(x=450, y=400)
                self.upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'M','I',self.member_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                self.upd_btn.place(x=400,y=480)

    def onProceedClick(self,parent,text):
        if(text=="PHONE NUMBER"):
            self.vav=tk.Label(parent,text="PHONE NUMBER: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
            self.vav.place(x=300,y=320)
            self.phno = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
            self.phno.place(x=480, y=320)
            self.clicked = StringVar()
            self.clicked.set("NAME")
            self.vax=tk.Label(parent,text="UPDATE? ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
            self.vax.place(x=300,y=370)
            self.upd_drop = tk.OptionMenu(parent,self.clicked,"NAME", "AGE","MEMBERSHIP")
            self.upd_drop.place(x=410, y=370)
            self.cont=tk.Button(parent,text="Continue",command=lambda: self.onContinueClick(parent,"PH",self.clicked.get(),self.phno.get()),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="GREEN")
            self.cont.place(x=550,y=370)
        else:
            self.vac=tk.Label(parent,text="CUSTOMER ID: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
            self.vac.place(x=300,y=320)
            self.id = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
            self.id.place(x=480, y=320)
            self.clicked = StringVar()
            self.clicked.set("NAME")
            self.vaa=tk.Label(parent,text="UPDATE? ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
            self.vaa.place(x=300,y=370)
            self.upd_drop = tk.OptionMenu(parent, self.clicked,"NAME", "AGE","MEMBERSHIP")
            self.upd_drop.place(x=410, y=370)
            self.cont=tk.Button(parent,text="Continue",command=lambda: self.onContinueClick(parent,"ID",self.clicked.get(),self.id),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="GREEN")
            self.cont.place(x=550,y=370)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        self.disp=tk.Label(parent,text="UPDATION", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        self.disp.place(x=400,y=170)
        self.upd_by=tk.Label(parent,text="UPDATE BY :",font=("Arial",20,"bold"),bg="#FFFDD0",fg="black").place(x=310,y=260)
        self.clicked=StringVar()
        self.clicked.set("PHONE NUMBER")
        self.upd_set_drop=tk.OptionMenu(parent,self.clicked,"ID","PHONE NUMBER")
        self.upd_set_drop.place(x=500,y=262)
        self.prcd_btn=tk.Button(parent, text="PROCEED",fg="white",width=7,height=1,bg="brown",command=lambda: self.onProceedClick(parent,self.clicked.get()),font=("Helventica", 10, "bold"))
        self.prcd_btn.place(x=650,y=263)
        self.back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        self.back.place(x=270,y=600)
