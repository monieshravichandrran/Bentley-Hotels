import tkinter as tk
from menu import Menu
from tkinter import messagebox
from PIL import ImageTk

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0,column=0,stick="nsew")
        self.bg=ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img=tk.Label(self,image=self.bg)
        self.bg_img.place(x=0,y=0,relwidth=1,relheight=1)
        box = LoginBox(self,controller)
        box.place(x=200,y=150,height=400,width=500)

class LoginBox(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent,bg="#FFFDD0",highlightbackground="black",highlightthickness=5)
        Frame1=tk.Label(parent,text="ADMIN LOGIN",bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold"))
        Frame1.place(x=280,y=170)
        Frame_user=tk.Label(parent,text="Email-id: ",bg="#FFFDD0",fg="black",font=("Arial",21,"bold"))
        Frame_user.place(x=250,y=270)
        self.user=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.user.place(x=400,y=275,width=250)
        Frame_pass=tk.Label(parent,text="Password: ",bg="#FFFDD0",fg="black",font=("Arial",19,"bold")).place(x=250,y=330)
        self.password=tk.Entry(parent,font=("Arial",15),bg="#FFFDD0",fg="black",show="*")
        self.password.place(x=400,y=335,width=250)
        Frame_submit=tk.Button(parent,text="LOGIN",command= lambda: self.onClickLogin(controller) ,font=("Helventica",15),bg="blue",fg="white",width=10,height=1)
        Frame_submit.place(x=250,y=380)
        Frame_forgot=tk.Label(parent,text="Forgot Password?",bg="#FFFDD0",fg="red",font=("Time New Roman",15)).place(x=250,y=475)

    def onClickLogin(self,controller):
        if self.user.get()=="abcd" and self.password.get()=="admin":
            messagebox.showinfo(title="Success",message="Login Successful.\n Press OK to continue")
            controller.show_frame(Menu)
        elif self.user.get()=="abcd" and self.password.get()!="admin":
            messagebox.showerror(title="Failure",message="Incorrect Password. Forgot Paaword?")
        else:
            messagebox.showerror(title="Failure",message="Incorrect admin mail")
