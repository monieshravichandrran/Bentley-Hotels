'''
    BILL CALCULATOR PAGE
'''
from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3
fbprice=0
check=False
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
        global fbprice
        global check
        fbprice=0
        check=False
        self.bill=Bill_Fram(self,controller)
        self.bill.place(x=10, y=10, height=770, width=1200)
class Bill_Fram(tk.Frame):
    def onClickEnd(self,parent,controller,stay):
        global  fbprice
        global check
        if check:
            from restaurantbill import total_price
            fbprice+=total_price
        else:
            check=True
        self.onADD['state']=DISABLED
        self.onEnd['state']=DISABLED
        stayprice=int(stay)*2500
        tk.Label(parent,text="YOUR BILL:",bg="#FFFDD0",fg="black",font=("Arial",25,"bold")).place(x=200,y=300)
        tk. Label(parent,text="STAY PRICE: "+str(round(stayprice,2))+" RS",bg="#FFFDD0",fg="black",font=("Arial",20,"bold")).place(x=400,y=350)
        tk.Label(parent, text="FOOD PRICE: " + str(round(fbprice,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(
            x=400, y=400)
        sercharge=int(stay)*250
        tk.Label(parent, text="SEVICE CHARGE: " + str(round(sercharge,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(
            x=400, y=450)
        expbill=stayprice+fbprice+sercharge
        sgst=0.18*(expbill)
        cgst=0.18*(expbill)
        conv=0.1*(expbill+cgst+sgst)
        tot=expbill+sgst+cgst+conv
        tk.Label(parent, text="SGST: " + str(round(sgst,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(
            x=400, y=500)
        tk.Label(parent, text="CGST: " + str(round(cgst,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(
            x=400, y=550)
        tk.Label(parent, text="MISC: " + str(round(conv,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(
            x=400, y=600)
        tk.Label(parent, text="TOTAL BILL: " + str(round(tot,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 30, "bold")).place(
            x=200, y=700)

    def onClickEnd1(self,parent,controller,stay,txt):
        global  fbprice
        global check
        if check:
            from restaurantbill import total_price
            fbprice+=total_price
        else:
            check=True
        self.onADD['state']=DISABLED
        self.onEnd['state']=DISABLED
        conn=sqlite3.connect('bentley.db')
        co=conn.cursor()
        co.execute('select member from customer where phone=?;',(txt,))
        l=co.fetchall()
        m=l[0][0]
        mem=StringVar()
        if(m=='V'):
            mem.set("VIP")
        elif m=="S":
            mem.set("SUPREME")
        else:
            mem.set("PRIME")
        con=conn.cursor()
        con.execute('select food,stay from membership where name=?;',(mem.get(),))
        sl=con.fetchall()
        fd=sl[0][0]
        sd=sl[0][1]
        stayprice=int(stay)*2500*(1-float(sd)/100)
        fbprice=fbprice*(1-float(fd)/100)
        tk.Label(parent,text="YOUR BILL:",bg="#FFFDD0",fg="black",font=("Arial",25,"bold")).place(x=200,y=300)
        tk. Label(parent,text="STAY PRICE: "+str(round(stayprice,2))+" RS",bg="#FFFDD0",fg="black",font=("Arial",20,"bold")).place(x=400,y=350)
        tk.Label(parent, text="FOOD PRICE: " + str(round(fbprice,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(
            x=400, y=400)
        sercharge=int(stay)*250
        tk.Label(parent, text="SEVICE CHARGE: " + str(round(sercharge,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(
            x=400, y=450)
        expbill=stayprice+fbprice+sercharge
        sgst=0.18*(expbill)
        cgst=0.18*(expbill)
        conv=0.1*(expbill+cgst+sgst)
        tot=expbill+sgst+cgst+conv
        tk.Label(parent, text="SGST: " + str(round(sgst,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(
            x=400, y=500)
        tk.Label(parent, text="CGST: " + str(round(cgst,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(
            x=400, y=550)
        tk.Label(parent, text="MISC: " + str(round(conv,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(
            x=400, y=600)
        tk.Label(parent, text="TOTAL BILL: " + str(round(tot,2))+" RS", bg="#FFFDD0", fg="black", font=("Arial", 30, "bold")).place(
            x=200, y=700)
    def onClickAdd1(self,parent,controller):
        global  fbprice
        global check
        controller.show_frame('FB')
        if check:
            from restaurantbill import total_price
            fbprice+=total_price
        else:
            check=True

    def onClickAdd(self,parent,controller):
        global  fbprice
        global check
        controller.show_frame('FB')
        if check:
            from restaurantbill import total_price
            fbprice+=total_price
        else:
            check=True

    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame('M')
    def onClickVal(self,parent,controller,txt):
        conn=sqlite3.connect('bentley.db')
        c=conn.cursor()
        c.execute('select phone from customer;')
        l=c.fetchall()
        li=list()
        for i in l:
            li.append(i[0])
        if txt not in li:
            tk.Label(parent,text="CUSTOMER DOESNOT EXIST!!! TRY AGAIN",bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(x=300,y=400)
        else:
            tk.Label(parent, text="STAY: ", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold")).place(x=200, y=200)
            self.stay_d1=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
            self.stay_d1.place(x=400,y=202)
            self.ab=tk.Label(parent,text="Add restaurant bill: ", bg="#FFFDD0", fg="black", font=("Arial", 15))
            self.ab.place(x=200,y=250)
            self.onADD=tk.Button(parent,text="CLICK",fg="white",width=7,height=1,bg="green",font=("Helventica", 15, "bold")
                                 ,command=lambda: self.onClickAdd1(parent,controller))
            self.onADD.place(x=440,y=250)
            self.onEnd=tk.Button(parent,text="END",fg="white",width=7,height=1,bg="red",font=("Helventica", 15, "bold")
                                 ,command=lambda: self.onClickEnd1(parent,controller,self.stay_d1.get(),txt))
            self.onEnd.place(x=570, y=250)
    def onClickValidate(self,parent,controller,text):
        self.valid_btn['state']=DISABLED
        if text=="MEMBER":
            tk.Label(parent,text="PHONE NO:",bg="#FFFDD0",fg="black",font=("Arial",20,"bold")).place(x=200,y=150)
            self.phno_d1=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
            self.phno_d1.place(x=400,y=155)
            self.val_btn=tk.Button(parent,text="CHECK",fg="white",width=7,height=1,bg="black",font=("Helventica", 15, "bold")
                                 ,command=lambda:self.onClickVal(parent,controller,self.phno_d1.get()))
            self.val_btn.place(x=700,y=150)
        else:
            stay=tk.Label(parent, text="STAY: ", bg="#FFFDD0", fg="black", font=("Arial", 20, "bold"))
            stay.place(x=200, y=150)
            self.stay_d2=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
            self.stay_d2.place(x=300,y=152)
            self.ab=tk.Label(parent,text="Add restaurant bill: ", bg="#FFFDD0", fg="black", font=("Arial", 15))
            self.ab.place(x=205,y=200)
            self.onADD=tk.Button(parent,text="CLICK",fg="white",width=7,height=1,bg="green",font=("Helventica", 15, "bold")
                                 ,command=lambda: self.onClickAdd(parent,controller))
            self.onADD.place(x=440,y=200)
            self.onEnd=tk.Button(parent,text="END",fg="white",width=7,height=1,bg="red",font=("Helventica", 15, "bold")
                                 ,command=lambda: self.onClickEnd(parent,controller,self.stay_d2.get()))
            self.onEnd.place(x=570, y=200)
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        tk.Label(parent,text="BILLING", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold")).place(x=450,y=20)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=40,y=730)
        self.clicked=StringVar()
        self.clicked.set("MEMBER")
        tk.Label(parent,text="CUSTOMER TYPE: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold")).place(x=200,y=100)
        self.bill_cust_drop=tk.OptionMenu(parent,self.clicked,"GUEST","MEMBER")
        self.bill_cust_drop.place(x=460,y=103)
        self.valid_btn=tk.Button(parent,text="CHECK",fg="white",width=10,height=1,bg="blue",font=("Helventica", 15, "bold"),
                                 command=lambda: self.onClickValidate(parent,controller,self.clicked.get()))
        self.valid_btn.place(x=600,y=100)
