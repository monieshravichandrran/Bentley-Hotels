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
        print(row)
        if type=="P":
            if text=="N":
                try:
                    c=conn.cursor()
                    c.execute('''
                            update customer set Name=? where phone=?;
                    ''',(get_val,checker))
                    eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300, y=540)
                except:
                    eu=tk.Label(parent,text="SPECIFIED PHONE NUMBER DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300, y=540)
            elif text=="A":
                try:
                    c=conn.cursor()
                    c.execute('''
                        update customer set Name=? where phone=?;
                        ''',(get_val,checker))
                    eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300,y=540)
                except:
                    eu=tk.Label(parent,text="SPECIFIED PHONE NUMBER DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300, y=540)
            else:
                try:
                    c=conn.cursor()
                    c.execute('''
                        update customer set member=? where phone=?;
                    ''',(get_val,checker))
                    eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300, y=540)
                except:
                    eu=tk.Label(parent,text="SPECIFIED PHONE NUMBER DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300, y=540)
        else:
            if text=="N":
                try:
                    c=conn.cursor()
                    c.execute('''
                                update customer set Name=? where id=?;
                            ''',(get_val,checker))
                    eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300, y=540)
                except:
                    eu=tk.Label(parent,text="SPECIFIED CUSTOMER ID DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300, y=540)
            elif text=="A":
                try:
                    c=conn.cursor()
                    c.execute('''
                                    update customer set age=? where id=?;
                             ''', (get_val, checker))
                    eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300, y=540)
                except:
                    eu=tk.Label(parent,text="SPECIFIED CUSTOMER ID DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300, y=540)
            else:
                try:
                    c=conn.cursor()
                    c.execute('''
                                    update customer set member=? where id=?;
                              ''', (get_val, checker))
                    eu = tk.Label(parent, text="UPDATION DONE SUCCESSFULLY",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300, y=540)
                except:
                    eu=tk.Label(parent,text="SPECIFIED CUSTOMER DOESNOT EXIST",font=("Arial",10,"bold"),bg="#FFFDD0",fg="black")
                    eu.place(x=300, y=540)
        conn.commit()
        conn.close()

    def onBackClick(self,controller):
        controller.show_frame("C")
    def onContinueClick(self,parent,type,text,checker):
        if type=="PH":
            if text=="NAME":
                x=tk.Label(parent,text="NAME: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=425)
                name_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                name_i.place(x=450,y=425)
                upd_btn=tk.Button(parent,text="UPDATE",font=("Helventica", 10, "bold"),command=lambda: self.onClickUpdate(parent,'N','P',name_i.get(),checker),fg="white",width=7,height=1,bg="blue")
                upd_btn.place(x=400,y=480)
            elif text=="AGE":
                x=tk.Label(parent,text="AGE: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=425)
                age_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                age_i.place(x=450, y=425)
                upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'A','P',age_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                upd_btn.place(x=400,y=480)
            else:
                x=tk.Label(parent,text="MEMBERSHIP: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=425)
                member_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                member_i.place(x=450, y=425)
                upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'M','P',member_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                upd_btn.place(x=400,y=480)
        else:
            if text=="NAME":
                x=tk.Label(parent,text="NAME: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=425)
                name_i=tk.Entry(parent,font=("Arial", 15), bg="#FFFDD0", fg="black")
                name_i.place(x=450, y=425)
                upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'N','I',name_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                upd_btn.place(x=400,y=480)
            elif text=="AGE":
                x = tk.Label(parent, text="AGE: ", font=("Arial", 15, "bold"), bg="#FFFDD0", fg="black").place(x=300,y=450)
                age_i = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
                age_i.place(x=450, y=400)
                upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'A','I',age_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                upd_btn.place(x=400,y=480)
            else:
                x = tk.Label(parent, text="AGE: ", font=("Arial", 15, "bold"), bg="#FFFDD0", fg="black").place(x=300,y=450)
                member_i = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
                member_i.place(x=450, y=400)
                upd_btn=tk.Button(parent,text="UPDATE",command=lambda: self.onClickUpdate(parent,'M','I',member_i.get(),checker),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="blue")
                upd_btn.place(x=400,y=480)

    def onProceedClick(self,parent,text):
        if(text=="PHONE NUMBER"):
            tk.Label(parent,text="PHONE NUMBER: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=320)
            self.phno = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
            self.phno.place(x=480, y=320)
            clicked = StringVar()
            clicked.set("NAME")
            tk.Label(parent,text="UPDATE? ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=370)
            upd_drop = tk.OptionMenu(parent, clicked,"NAME", "AGE","MEMBERSHIP")
            upd_drop.place(x=410, y=370)
            cont=tk.Button(parent,text="Continue",command=lambda: self.onContinueClick(parent,"PH",clicked.get(),self.phno.get()),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="GREEN")
            cont.place(x=550,y=370)
        else:
            tk.Label(parent,text="CUSTOMER ID: ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=320)
            self.id = tk.Entry(parent, font=("Arial", 15), bg="#FFFDD0", fg="black")
            self.id.place(x=480, y=320)
            clicked = StringVar()
            clicked.set("NAME")
            tk.Label(parent,text="UPDATE? ",font=("Arial",15,"bold"),bg="#FFFDD0",fg="black").place(x=300,y=370)
            upd_drop = tk.OptionMenu(parent, clicked,"NAME", "AGE","MEMBERSHIP")
            upd_drop.place(x=410, y=370)
            cont=tk.Button(parent,text="Continue",command=lambda: self.onContinueClick(parent,"ID",clicked.get(),self.id),font=("Helventica", 10, "bold"),fg="white",width=7,height=1,bg="GREEN")
            cont.place(x=550,y=370)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="UPDATION", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=400,y=170)
        upd_by=tk.Label(parent,text="UPDATE BY :",font=("Arial",20,"bold"),bg="#FFFDD0",fg="black").place(x=310,y=260)
        clicked=StringVar()
        clicked.set("PHONE NUMBER")
        upd_set_drop=tk.OptionMenu(parent,clicked,"ID","PHONE NUMBER")
        upd_set_drop.place(x=500,y=262)
        prcd_btn=tk.Button(parent, text="PROCEED",fg="white",width=7,height=1,bg="brown",command=lambda: self.onProceedClick(parent,clicked.get()),font=("Helventica", 10, "bold"))
        prcd_btn.place(x=650,y=263)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(controller))
        back.place(x=270,y=600)
