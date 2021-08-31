from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3
total_price=0
class Restaurant_Bill(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.resbill=Restaurant_Bill_Fram(self,controller)
        self.resbill.place(x=250,y=150,height=500,width=600)
    def reset(self,controller):
        del self.resbill
        self.resbill=Restaurant_Bill_Fram(self,controller)
        self.resbill.place(x=250,y=150,height=500,width=600)

class Restaurant_Bill_Fram(tk.Frame):
    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("B")
    def onClickCalc(self,parent,controller,name,qty):
        global total_price
        self.calculate['state']=DISABLED
        conn=sqlite3.connect('bentley.db')
        try:
            c=conn.cursor()
            c.execute('''
                select * from restaurant where name=?;
            ''',(name,))
            l=c.fetchall()
            price=l[0][3]
            total_price=float(price)*int(qty)
            self.eu = tk.Label(parent, text="COMPUTED!!\nCLICK BACK TO ADD MORE TO CART", font=("Arial", 10, "bold"), bg="#FFFDD0",
                          fg="black")
            self.eu.place(x=300, y=550)
            print(total_price)
        except:
            self.eu = tk.Label(parent, text="NO SUCH ITEM EXISTS!!!\nCLICK BACK TO CONTINUE BILL CALCULATION", font=("Arial", 10, "bold"), bg="#FFFDD0",
                          fg="black")
            self.eu.place(x=300, y=550)
            total_price=0
        conn.commit()
        conn.close()
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        tk.Label(parent,text="FOOD BILLING", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold")).place(x=400,y=170)
        name_d=tk.Label(parent,text="NAME: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        name_d.place(x=330,y=260)
        self.name_d=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.name_d.place(x=460,y=265)
        qty_d=tk.Label(parent,text="QTY: ",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        qty_d.place(x=330,y=380)
        self.qty_d=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.qty_d.place(x=460,y=385)
        self.calculate=tk.Button(parent,text="COMPUTE",fg="white",width=10,height=1,bg="green",font=("Helventica", 15, "bold"),
                                 command=lambda: self.onClickCalc(parent,controller,self.name_d.get(),self.qty_d.get()))
        self.calculate.place(x=300,y=450)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=270,y=600)
