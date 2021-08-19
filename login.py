#importing necessary python libraries
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk

class Login:

    def __init__(self,root):
        self.root=root
        self.islog=False

        #Setup background Image
        self.bg=ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Setup Login Frame
        Frame_Login=Frame(self.root,bg="#FFFDD0",highlightbackground="black",highlightthickness=5).place(x=200,y=150,height=400,width=500)
        Frame_1=Label(Frame_Login,text="ADMIN LOGIN",bg="#FFFDD0",fg="#F99B03",font=("Helventica",35,"bold")).place(x=280,y=170)
        Frame_user=Label(Frame_Login,text="Email-id: ",bg="#FFFDD0",fg="black",font=("Arial",21,"bold")).place(x=250,y=270)
        self.user=Entry(Frame_Login,font=("Arial",15),bg="#FFFDD0",fg="black")
        self.user.place(x=400,y=275,width=250)
        Frame_pass=Label(Frame_Login,text="Password: ",bg="#FFFDD0",fg="black",font=("Arial",19,"bold")).place(x=250,y=330)
        self.password=Entry(Frame_Login,font=("Arial",15),bg="#FFFDD0",fg="black",show="*")
        self.password.place(x=400,y=335,width=250)
        Frame_submit=Button(Frame_Login,text="LOGIN",command=self.onClickLogin,font=("Helventica",15),bg="blue",fg="white",width=10,height=1).place(x=250,y=380)
        Frame_forgot=Label(Frame_Login,text="Forgot Password?",bg="#FFFDD0",fg="red",font=("Time New Roman",15)).place(x=250,y=475)

    def onClickLogin(self):
        if self.user.get()=="abcd" and self.password.get()=="admin":
            self.islog=True
            messagebox.showinfo(title="Success",message="Login Successful")
        elif self.user.get()=="abcd" and self.password.get()!="admin":
            messagebox.showerror(title="Failure",message="Incorrect Password. Forgot Paaword?")
        else:
            messagebox.showerror(title="Failure",message="Incorrect admin mail")
