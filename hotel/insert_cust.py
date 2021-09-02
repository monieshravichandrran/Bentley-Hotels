'''
Insert Customer page
'''
from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3

class Ins_cust(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.ins=Ins_cust_Fram(self,controller)
        self.ins.place(x=250,y=150,height=500,width=600)
    def reset(self,controller):
        del self.ins
        self.ins=Ins_cust_Fram(self,controller)
        self.ins.place(x=250,y=150,height=500,width=600)

class Ins_cust_Fram(tk.Frame):
    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("C")
    def onClickInsert(self,parent,name,age,phno,member):
        self.ins_btn['state']=DISABLED
        conn=sqlite3.connect('bentley.db')
        c=conn.cursor()
        t=conn.cursor()
        t.execute('SELECT max(id) FROM CUSTOMER;')
        l=t.fetchall()
        membership=StringVar()
        membership.set("N")
        if member=="SUPREME":
            membership.set("S")
        elif member=="PRIME":
            membership.set("P")
        elif member=="VIP":
            membership.set("V")
        id=l[0][0]+1
        members=membership.get()
        try:
            c.execute('''
                    insert into customer values(?,?,?,?,?);
            ''',(id,name,int(age),members,phno))
            self.eu = tk.Label(parent, text="INSERTION DONE SUCCESSFULLY", font=("Arial", 10, "bold"), bg="#FFFDD0",
                          fg="black")
            self.eu.place(x=300, y=550)
            conn.commit()
            conn.close()
        except:
            txt=StringVar()
            if len(name)==0:
                txt.set("INSERTION FAILED!!! ENTER NAME")
            elif int(age)<18:
                txt.set("INSERTION FAILED!!! INVALID AGE")
            elif len(phno)!=10:
                txt.set("INSERTION FAILED!!! INVALID PHONE NUMBER")
            elif int(age)<18:
                txt.set("INSERTION FAILED!!! INVALID AGE")
            elif members=="N":
                txt.set("INSERTION FAILED!!! INVALID MEMBERSHIP")
            else:
                txt.set("INSERTION FAILED!!! PHONE NUMBER ALREADY EXISTS")
            self.eu = tk.Label(parent, text=txt.get(), font=("Arial", 10, "bold"), bg="#FFFDD0",
                          fg="black")
            self.eu.place(x=300, y=550)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="INSERTION", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=400,y=170)
        name_d=tk.Label(parent,text="NAME: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        name_d.place(x=330,y=260)
        self.name=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.name.place(x=460,y=265)
        age_d=tk.Label(parent,text="AGE: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        age_d.place(x=330,y=320)
        self.age=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.age.place(x=460,y=325)
        phno_d=tk.Label(parent,text="PHONE: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        phno_d.place(x=330,y=380)
        self.phno=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.phno.place(x=460,y=385)
        member_d=tk.Label(parent,text="MEMBER: ",bg="#FFFDD0",fg="black",font=("Arial",19,"bold"))
        member_d.place(x=330,y=435)
        self.member=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.member.place(x=460,y=440)
        self.ins_btn=tk.Button(parent, text="INSERT",fg="white",width=10,height=1,bg="blue",font=("Helventica", 15, "bold"),command=lambda: self.onClickInsert(parent,self.name.get(),self.age.get(),self.phno.get(),self.member.get()))
        self.ins_btn.place(x=330,y=480)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=270,y=600)
