#importing necessary python libraries
from tkinter import*
from login import Login
from menu import Menu

root=Tk()
root.title("Bentley Hotels")
root.iconbitmap("images/logo.png")
root.geometry("1219x800+100+0")
root.resizable(False, False)
obj=Login(root)
if obj.islog:
    obj1=Menu(root)
root.mainloop()
