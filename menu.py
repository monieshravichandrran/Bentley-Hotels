#importing necessary python libraries
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk

class Menu:
    def __init__(self,Frame2):
        self.Frame2=Frame2
        self.bg = ImageTk.PhotoImage(file="images/logo.png")
        self.bg_img = Label(self.Frame2, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        
