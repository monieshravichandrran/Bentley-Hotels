'''
    BILL CALCULATOR PAGE
'''
from tkinter import *
import tkinter as tk
from PIL import ImageTk

class Bill(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.bill=Bill_Fram(self,controller)
        self.bill.place(x=10,y=10,height=770,width=1200)
    def reset(self,controller):
        del self.bill
        self.bill=Bill_Fram(self,controller)
        self.bill.place(x=10, y=10, height=770, width=1200)
class Bill_Fram(tk.Frame):
    def onClickAdd(self,parent,controller):
        controller.show_frame('FB')
    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("M")
    def onClickValidate(self,parent,controller,text):
        self.valid_btn['state']=DISABLED
        if text=="MEMBER":
            tk.Label(parent,text="PHONE NO:",bg="#FFFDD0",fg="black",font=("Arial",20,"bold")).place(x=200,y=150)
            self.phno_d1=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
            self.phno_d1.place(x=400,y=152)
            tk.Label(parent, text="STAY: ", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(x=200, y=200)
            self.stay_d1=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
            self.stay_d1.place(x=400,y=202)
        else:
            stay=tk.Label(parent, text="STAY: ", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold"))
            stay.place(x=200, y=150)
            self.stay_d2=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
            self.stay_d2.place(x=300,y=152)
            self.ab=tk.Label(parent,text="Add restaurant details: ", bg="#FFFDD0", fg="black", font=("Arial", 15))
            self.ab.place(x=205,y=200)
            self.onADD=tk.Button(parent,text="CLICK",fg="white",width=7,height=1,bg="green",font=("Helventica", 15, "bold")
                                 ,command=lambda: self.onClickAdd(parent,controller))
            self.onADD.place(x=440,y=200)
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        tk.Label(parent,text="BILLING", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold")).place(x=450,y=20)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=40,y=750)
        self.clicked=StringVar()
        self.clicked.set("MEMBER")
        tk.Label(parent,text="CUSTOMER TYPE: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold")).place(x=200,y=100)
        self.bill_cust_drop=tk.OptionMenu(parent,self.clicked,"GUEST","MEMBER")
        self.bill_cust_drop.place(x=460,y=103)
        self.valid_btn=tk.Button(parent,text="CHECK",fg="white",width=10,height=1,bg="blue",font=("Helventica", 15, "bold"),
                                 command=lambda: self.onClickValidate(parent,controller,self.clicked.get()))
        self.valid_btn.place(x=600,y=100)
