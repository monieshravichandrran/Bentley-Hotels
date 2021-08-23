import tkinter as tk
from PIL import ImageTk
import time

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        cust=MenuBars(self,controller,"Customer")
        cust.place(x=170,y=70,height=300,width=350)
        emp=MenuBars(self,controller,"Bill")
        emp.place(x=570,y=70,height=300,width=350)
        Bill=MenuBars(self,controller,"Hotel")
        Bill.place(x=170,y=420,height=300,width=350)
        logout=MenuBars(self,controller,"Logout")
        logout.place(x=570,y=420,height=300,width=350)

class MenuBars(tk.Frame):
    def Cust(self,controller):
        controller.show_frame("C")
    def Billl(self,controller):
        controller.show_frame("B")
    def Hotell(self,controller):
        controller.show_frame("H")
    def lgout(self,controller):
        time.sleep(0.1)
        controller.show_frame("Lg")
    def __init__(self,parent,controller,txt):
        tk.Frame.__init__(self,parent,bg="#FFFDD0",highlightbackground="black",highlightthickness=5)
        if txt=="Customer":
            B=tk.Button(parent,text=txt+"\nManagement",width=27,height=11,bg="#FFFDD0",font=("Helventica",15,"bold"),command=lambda:self.Cust(controller)).place(x=180,y=80)
        elif txt=="Bill":
            B=tk.Button(parent,text=txt+"\nCalcuator",width=27,height=11,bg="#FFFDD0",font=("Helventica",15,"bold"),command=lambda:self.Billl(controller)).place(x=580,y=80)
        elif txt=="Hotel":
            B=tk.Button(parent,text=txt+"\nManagement",width=27,height=11,bg="#FFFDD0",font=("Helventica",15,"bold"),command=lambda:self.Hotell(controller)).place(x=180,y=430)
        else:
            B=tk.Button(parent,text=txt,width=27,height=11,bg="#FFFDD0",font=("Helventica",15,"bold"),command=lambda:self.lgout(controller)).place(x=580,y=430)
