'''                                          ''

                THE BENTLEY HOTELS
    
        HOTEL MANAGEMENT SYSTEM
        BUILT ON TKinter and SQLITE
        
        BY: MONIESH.R 
            BE COMPUTER SCIENCE
            SSN COLLEGE OF ENGINEERING 
 
'''                                          ''

#Required Header Files
import tkinter as tk
from tkinter import *
from login import Login
from menu import Menu
from customer import Customer
from bill import Bill
from hotel import Hotel
from insert_cust import Ins_cust
from update_cust import Upd_cust
from del_cust import Del_cust
#Dictionary to keep track of the Frames with a identifier as their key

frame_name={"Lg":Login,"M":Menu,"C":Customer,"B":Bill,"H":Hotel,
            "CU":Upd_cust,"CI":Ins_cust,"CD":Del_cust}
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        #Setting up title,icon & dimensions of our app
        self.title("Bentley Hotels")
        self.iconbitmap("images/logo.png")
        self.geometry("1219x800+100+0")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.frame_list=[Login,Menu,Customer,Bill,Hotel,Ins_cust,Upd_cust,Del_cust]
        for F in (self.frame_list):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Lg")

    #Function to raise the desired Frame
    def show_frame(self, cont):
        global frame_name
        frame = self.frames[frame_name[cont]]
        frame.tkraise()

app = App()
app.mainloop()
