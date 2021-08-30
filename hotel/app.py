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
from staff import Staff
from restaurant import Restaurant
from insert_staff import Ins_staff
from update_staff import Upd_staff
from delete_staff import Del_staff
from insert_rs import Ins_rs
from update_rs import Upd_rs
from delete_rs import Del_rs
from package_management import Pack
from restaurantbill import Restaurant_Bill
#Dictionary to keep track of the Frames with a identifier as their key

frame_name={"Lg":Login,"M":Menu,"C":Customer,"B":Bill,"H":Hotel,
            "CU":Upd_cust,"CI":Ins_cust,"CD":Del_cust,"S":Staff,"R":Restaurant,
            "SI":Ins_staff,"SU":Upd_staff,"SD":Del_staff,"RI":Ins_rs,"RU":Upd_rs,"RD":Del_rs,"P":Pack,"FB":Restaurant_Bill}
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        #Setting up title,icon & dimensions of our app
        self.title("Bentley Hotels")
        self.iconbitmap("images/logo.png")
        self.geometry("1219x800+100+0")
        self.resizable(False,False)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.frame_list=[Login,Menu,Customer,Bill,Hotel,Ins_cust,Upd_cust,Del_cust,Staff,Restaurant,
                         Ins_staff,Upd_staff,Del_staff,Ins_rs,Upd_rs,Del_rs,Pack,Restaurant_Bill]
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
