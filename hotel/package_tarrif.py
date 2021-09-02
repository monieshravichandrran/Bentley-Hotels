'''
Package tarrif page
'''
import tkinter as tk
from PIL import ImageTk
import sqlite3

class View_pack(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        self.view=View_pack_Fram(self,controller)
        self.view.place(x=250,y=150,height=500,width=600)
    def reset(self,controller):
        del self.view
        self.view=View_pack_Fram(self,controller)
        self.view.place(x=250,y=150,height=500,width=600)

class View_pack_Fram(tk.Frame):
    def onBackClick(self,parent,controller):
        parent.reset(controller)
        controller.show_frame("H")
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        disp=tk.Label(parent,text="VIEW PACKAGE", bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        disp.place(x=390,y=170)
        conn=sqlite3.connect('bentley.db')
        c=conn.cursor()
        c.execute('select * from membership;')
        l=c.fetchall()
        tk.Label(parent,text="MEMBERSHIP"+"    "+"STAY DIS"+"    "+"FOOD DISC"
                 ,bg="#FFFDD0",fg="black",font=("Arial",20,"bold")).place(x=270,y=250)
        eu1=tk.Label(parent,text="       "+l[0][0]+"                    "+str(l[0][1])+"%               "+str(l[0][2])+"%"
                    ,bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        eu1.place(x=270,y=320)
        eu2=tk.Label(parent,text="       "+l[1][0]+"              "+str(l[1][1])+"%               "+str(l[1][2])+"%"
                    ,bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        eu2.place(x=270,y=370)
        eu3=tk.Label(parent,text="       "+l[2][0]+"         "+str(l[2][1])+"%              "+str(l[2][2])+"%",bg="#FFFDD0",fg="black",font=("Arial",20,"bold"))
        eu3.place(x=270,y=420)
        back=tk.Button(parent,text="BACK",fg="white",bg="red",command=lambda: self.onBackClick(parent,controller))
        back.place(x=270,y=600)