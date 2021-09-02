'''
    WELCOME TO LOGIN PAGE OF BENTLEY HOTELS
'''

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import sqlite3
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0,column=0,stick="nsew")
        self.bg=ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img=tk.Label(self,image=self.bg)
        self.bg_img.place(x=0,y=0,relwidth=1,relheight=1)
        self.box = LoginBox(self,controller)
        self.box.place(x=200,y=150,height=400,width=500)
class LoginBox(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent,bg="#FFFDD0",highlightbackground="black",highlightthickness=5)
        Frame1=tk.Label(parent,text="ADMIN LOGIN",bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        Frame1.place(x=280,y=170)
        Frame_user=tk.Label(parent,text="Username: ",bg="#FFFDD0",fg="black",font=("Arial",19,"bold"))
        Frame_user.place(x=250,y=270)
        self.user=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.user.place(x=400,y=275,width=250)
        Frame_pass=tk.Label(parent,text="Password: ",bg="#FFFDD0",fg="black",font=("Arial",19,"bold")).place(x=250,y=330)
        self.password=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black",show="*")
        self.password.place(x=400,y=335,width=250)
        Frame_submit=tk.Button(parent,text="LOGIN",command= lambda: self.onClickLogin(parent,controller) ,font=("Helventica",15),bg="blue",fg="white",width=10,height=1)
        Frame_submit.place(x=250,y=380)
        Frame_forgot=tk.Label(parent,text="WELCOME TO BENTLEY HOTELS \nLOGIN TO CONTINUE!!!",bg="#FFFDD0",fg="red",font=("Time New Roman",15)).place(x=250,y=460)

    def onClickLogin(self,parent,controller):
        conn=sqlite3.connect('bentley.db')
        c=conn.cursor()
        c.execute('select * from admin')
        l=c.fetchall()
        if self.user.get()==l[0][0] and self.password.get()==l[0][1]:
            messagebox.showinfo(title="Success",message="Login Successful.\nPress OK to continue")
            self.__init__(parent,controller)
            controller.show_frame("M")
        elif self.user.get()==l[0][0] and self.password.get()!=l[0][1]:
            messagebox.showerror(title="Failure",message="Incorrect Password")
        else:
            messagebox.showerror(title="Failure",message="Incorrect admin mail")
        conn.commit()
        conn.close()
