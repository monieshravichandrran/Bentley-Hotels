'''
Security page
'''
from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3

class Security(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.view=Sec_Fram(self,controller)
        self.view.place(x=250,y=150,height=500,width=600)
    def reset(self,controller):
        del self.view
        self.view=Sec_Fram(self,controller)
        self.view.place(x=250,y=150,height=500,width=600)

class Sec_Fram(tk.Frame):
    def onClickUpdate(self,parent,username,password,txt):
        self.upd_btn['state']=DISABLED
        try:
            conn=sqlite3.connect('bentley.db')
            c=conn.cursor()
            c.execute("update admin set username=?,password=? where password=?",(username.get(),password.get(),txt,))
            tk.Label(parent,text="UPDATED!!! CLICK BACK TO CONTINUE",font=("Arial", 15, "bold"), bg="#FFFDD0",
                          fg="black").place(x=290,y=550)
        except:
            tk.Label(parent,text="INVALID USERNAME OR PASSWORD",font=("Arial", 15, "bold"), bg="#FFFDD0",
                          fg="black").place(x=290,y=550)
        conn.commit()
        conn.close()
    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("M")
    def onValidClick(self,parent,txt):
        self.prd_btn['state']=DISABLED
        conn=sqlite3.connect('bentley.db')
        c=conn.cursor()
        c.execute('select * from admin where password=?',(txt,))
        l=c.fetchall()
        if len(l)==0:
            tk.Label(parent,text="INVALID PASSWORD!!!",font=("Arial", 20, "bold"), bg="#FFFDD0",
                          fg="black").place(x=300,y=440)
        else:
            tk.Label(parent,text="New Username: ",font=("Arial", 15, "bold"), bg="#FFFDD0",
                          fg="black").place(x=300,y=350)
            self.user_name=tk.Entry(parent,font=("Arial", 15, "bold"), bg="#FFFDD0",
                          fg="black")
            self.user_name.place(x=500,y=350)
            tk.Label(parent,text="New Password: ",font=("Arial", 15, "bold"), bg="#FFFDD0",
                          fg="black").place(x=300,y=450)
            self.password=tk.Entry(parent,font=("Arial", 15, "bold"), bg="#FFFDD0",
                          fg="black",show="*")
            self.password.place(x=500,y=450)
            self.upd_btn=tk.Button(parent, text="UPDATE",fg="white",width=10,height=1,bg="blue",
                                   font=("Helventica", 15, "bold"),
                                   command=lambda: self.onClickUpdate(parent,self.user_name,self.password,txt))
            self.upd_btn.place(x=330,y=480)
        conn.commit()
        conn.close()
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="SECURITY", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=390,y=170)
        pass_d=tk.Label(parent,text="Password: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        pass_d.place(x=330,y=260)
        self.psd=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black",show="*")
        self.psd.place(x=480,y=265)
        self.prd_btn=tk.Button(parent, text="VALIDATE",fg="white",width=8,height=1,bg="brown",font=("Helventica", 10, "bold"),
                               command=lambda: self.onValidClick(parent,self.psd.get()))
        self.prd_btn.place(x=630,y=300)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=270,y=600)