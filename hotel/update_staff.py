'''
Update Staff page
'''
from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3
class Upd_staff(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.upd=Upd_staff_Fram(self,controller)
        self.upd.place(x=250,y=150,height=500,width=600)
    def reset(self,controller):
        del self.upd
        self.upd=Upd_staff_Fram(self,controller)
        self.upd.place(x=250,y=150, height=500, width=600)

class Upd_staff_Fram(tk.Frame):
    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("S")
    def onClickUpdate(self,parent,text,Type,checker,get_val):
        self.upd_btn['state']=DISABLED
        conn=sqlite3.connect('bentley.db')
        txtt=StringVar()
        if Type=="P":
            ch=conn.cursor()
            ch.execute('select phone from staff;')
            rs1=ch.fetchall()
            rs=list()
            for i in rs1:
                rs.append(i[0])
            print(rs)
            if get_val not in rs:
                self.eu = tk.Label(parent, text="SPECIFIED PHONE NUMBER DOESNOT EXIST",font=("Arial", 10, "bold"), bg="#FFFDD0", fg="black")
                self.eu.place(x=300, y=540)
                return
            if text=="N":
                try:
                    c=conn.cursor()
                    c.execute('''
                            update staff set name=? where phone=?;
                    ''',(checker,get_val,))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
                except:
                    if(len(checker)==0):
                       txtt.set("UPDATION FAILED!!! INVALID NAME ENTERED")
                       self.eu=tk.Label(parent,text=txtt.get(),font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                       self.eu.place(x=300, y=540)
            elif text=="A":
                try:
                    c=conn.cursor()
                    c.execute('''
                        update staff set age=? where phone=?;
                        ''',(int(checker),get_val,))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300,y=540)
                except:
                    if int(checker)<18:
                        txtt.set("UPDATION FAILED!!! INVALID AGE ENTERED")
                    self.eu = tk.Label(parent, text=txtt.get(), font=("Arial", 10, "bold"), bg="#FFFDD0",
                                           fg="black")
                    self.eu.place(x=300, y=540)
            else:
                try:
                    c=conn.cursor()
                    c.execute('''
                        update staff set salary=? where phone=?;
                    ''',(checker,get_val,))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
                except:
                    if len(checker)==0:
                        txtt.set("UPDATION FAILED!!! INVALID SALARY ENTERED")
                    self.eu = tk.Label(parent, text=txtt.get(), font=("Arial", 10, "bold"), bg="#FFFDD0",
                                           fg="black")
                    self.eu.place(x=300, y=540)
        else:
            ch=conn.cursor()
            ch.execute('select id from staff;')
            rs1=ch.fetchall()
            rs=list()
            for i in rs1:
                rs.append(i[0])
            if int(get_val) not in rs:
                self.eu = tk.Label(parent, text="SPECIFIED CUSTOMER ID DOESNOT EXIST",font=("Arial", 10, "bold"), bg="#FFFDD0", fg="black")
                self.eu.place(x=300, y=540)
                return
            if text=="N":
                try:
                    c=conn.cursor()
                    c.execute('''
                                update staff set Name=? where id=?;
                            ''',(checker,int(get_val),))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
                except:
                    if(len(checker)==0):
                       txtt.set("UPDATION FAILED!!! INVALID NAME ENTERED")
                       self.eu=tk.Label(parent,text=txtt.get(),font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                       self.eu.place(x=300, y=540)
            elif text=="A":
                try:
                    c=conn.cursor()
                    c.execute('''
                                    update staff set age=? where id=?;
                             ''', (int(checker), int(get_val),))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
                except:
                    if int(checker)<18:
                        txtt.set("UPDATION FAILED!!! INVALID AGE ENTERED")
                    self.eu = tk.Label(parent, text=txtt.get(), font=("Arial", 10, "bold"), bg="#FFFDD0",
                                           fg="black")
                    self.eu.place(x=300, y=540)
            else:
                try:
                    c=conn.cursor()
                    c.execute('''
                                    update staff set salary=? where id=?;
                              ''', (checker, int(get_val),))
                    self.eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    self.eu.place(x=300, y=540)
                except:
                    if len(checker)==0:
                        txtt.set("UPDATION FAILED!!! INVALID SALARY ENTERED")
                    self.eu = tk.Label(parent, text=txtt.get(), font=("Arial", 10, "bold"), bg="#FFFDD0",
                                           fg="black")
                    self.eu.place(x=300, y=540)
        conn.commit()
        conn.close()
    def onContinueClick(self,parent,type,text,checker):
        self.cont['state']=DISABLED
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
                self.x=tk.Label(parent,text="SALARY: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
                self.x.place(x=300,y=425)
                self.salary_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                self.salary_i.place(x=450, y=425)
                self.upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'S','P',self.salary_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
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
                self.x.place(x=300,y=425)
                self.age_i = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
                self.age_i.place(x=450, y=425)
                self.upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'A','I',self.age_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                self.upd_btn.place(x=400,y=480)
            else:
                self.x = tk.Label(parent, text="SALARY: ", font=("Arial", 15, "bold"), bg="#FFFDD0", fg="black")
                self.x.place(x=300,y=425)
                self.salary_i = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
                self.salary_i.place(x=450, y=425)
                self.upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'M','I',self.salary_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                self.upd_btn.place(x=400,y=480)

    def onProceedClick(self,parent,txt):
        self.prcd_btn['state']=DISABLED
        if txt=="PHONE NUMBER":
            self.vav=tk.Label(parent,text="PHONE NUMBER: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
            self.vav.place(x=300,y=320)
            self.phno = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
            self.phno.place(x=480, y=320)
            self.clicked = StringVar()
            self.clicked.set("NAME")
            self.vax=tk.Label(parent,text="UPDATE? ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
            self.vax.place(x=300,y=370)
            self.upd_drop = tk.OptionMenu(parent,self.clicked,"NAME", "AGE","SALARY")
            self.upd_drop.place(x=410, y=370)
            self.cont=tk.Button(parent,text="Continue",command=lambda: self.onContinueClick(parent,"PH",self.clicked.get(),self.phno.get()),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="GREEN")
            self.cont.place(x=550,y=370)
        else:
            self.vav=tk.Label(parent,text="STAFF ID: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
            self.vav.place(x=300,y=320)
            self.phno = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
            self.phno.place(x=480, y=320)
            self.clicked = StringVar()
            self.clicked.set("NAME")
            self.vax=tk.Label(parent,text="UPDATE? ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black")
            self.vax.place(x=300,y=370)
            self.upd_drop = tk.OptionMenu(parent,self.clicked,"NAME", "AGE","SALARY")
            self.upd_drop.place(x=410, y=370)
            self.cont=tk.Button(parent,text="Continue",command=lambda: self.onContinueClick(parent,"ID",self.clicked.get(),self.phno.get()),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="GREEN")
            self.cont.place(x=550,y=370)

    def __init__(self,parent,controller):
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
