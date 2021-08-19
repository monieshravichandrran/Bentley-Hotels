#importing necessary python libraries
import tkinter as tk
from login import Login
from menu import Menu

window=tk.Tk()
window.title("Bentley Hotels")
window.iconbitmap("images/logo.png")
window.geometry("1219x800+100+0")
#window.resizable(False, False)
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
Frame1=tk.Frame(window)
obj1=Login(Frame1)
if obj1.islog:
    Frame2=tk.Frame(window)
    obj2=Menu(Frame2)
window.mainloop()
