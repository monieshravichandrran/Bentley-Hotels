'''
Package Management Page
'''
from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3

class Pack(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.pck=Pack_Fram(self,controller)
        self.pck.place(x=250,y=150,height=500,width=600)
    def reset(self,controller):
        del self.pck
        self.pck=Pack_Fram(self,controller)
        self.pck.place(x=250,y=150,height=500,width=600)

class Pack_Fram(tk.Frame):
    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("H")
    def onClickManage(self,parent,member,food,stay):
        self.mng_btn['state']=DISABLED
        conn=sqlite3.connect('bentley.db')
        c=conn.cursor()
        t=conn.cursor()
        t.execute('select name from membership;')
        l=t.fetchall()
        li=list()
        xx=conn.cursor()
        xx.execute('select * from membership;')
        lx=xx.fetchall()
        print(lx)
        for i in l:
            li.append(i[0])
        if member not in li:
            self.eu = tk.Label(parent, text="SPECIFIED MEMBERSHIP DOESNOT EXIST", font=("Arial", 10, "bold"),
                               bg="#FFFDD0", fg="black")
            self.eu.place(x=300, y=540)
            return
        try:
            c.execute('''
                update membership set food=?,stay=? where name=?;
            ''',(food,stay,member))
            self.eu = tk.Label(parent, text="MEMBERSHIP UPDATION SUCCESSFULL!!!", font=("Arial", 10, "bold"),
                               bg="#FFFDD0", fg="black")
            self.eu.place(x=300, y=540)
        except:
            self.eu = tk.Label(parent, text="SPECIFIED MEMBERSHIP DOESNOT EXIST", font=("Arial", 10, "bold"),
                               bg="#FFFDD0", fg="black")
            self.eu.place(x=300, y=540)
        conn.commit()
        conn.close()
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="PACKAGE", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=400,y=170)
        member_d=tk.Label(parent,text="MEMBER: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        member_d.place(x=330,y=260)
        self.member_d=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.member_d.place(x=460,y=265)
        food_d=tk.Label(parent,text="FOOD : ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        food_d.place(x=330,y=320)
        self.food_d=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.food_d.place(x=460,y=325)
        stay_d=tk.Label(parent,text="STAY : ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        stay_d.place(x=330,y=380)
        self.stay_d=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.stay_d.place(x=460,y=385)
        self.mng_btn=tk.Button(parent, text="MANAGE",fg="white",width=10,height=1,bg="blue",font=("Helventica", 15, "bold"),command=lambda: self.onClickManage(parent,self.member_d.get(),self.food_d.get(),self.stay_d.get()))
        self.mng_btn.place(x=330,y=480)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=270,y=600)
