'''
Staff management page
'''
import tkinter as tk
from PIL import ImageTk

class Staff(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        ins_staff=Staff_Fram(self,controller,"Insert")
        ins_staff.place(x=170, y=70, height=300, width=350)
        upd_staff=Staff_Fram(self,controller,"Update")
        upd_staff.place(x=570, y=70, height=300, width=350)
        del_staff=Staff_Fram(self,controller,"Delete")
        del_staff.place(x=170, y=420, height=300, width=350)
        view=Staff_Fram(self,controller,"View")
        view.place(x=570, y=420, height=300, width=350)

class Staff_Fram(tk.Frame):
    def stbackclick(self,controller):
        controller.show_frame("H")
    def stupdclick(self,controller):
        controller.show_frame("SU")
    def stinsclick(self,controller):
        controller.show_frame("SI")
    def stdelclick(self,controller):
        controller.show_frame("SD")
    def stViewClick(self,controller):
        controller.show_frame("SV")
    def __init__(self,parent,controller,txt):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        if txt == "Insert":
            B = tk.Button(parent, text=txt + "\nStaff", width=27, height=11, bg="#FFFDD0",
                          font=("Helventica", 15, "bold"),command=lambda: self.stinsclick(controller)).place(x=180, y=80)
        elif txt == "Update":
            B = tk.Button(parent, text=txt + "\nStaff", width=27, height=11, bg="#FFFDD0",
                          font=("Helventica", 15, "bold"),command=lambda: self.stupdclick(controller)).place(x=580, y=80)
        elif txt == "Delete":
            B = tk.Button(parent, text=txt + "\nStaff", width=27, height=11, bg="#FFFDD0",
                          font=("Helventica", 15, "bold"),command=lambda: self.stdelclick(controller)).place(x=180, y=430)
        elif txt=="View":
            B = tk.Button(parent, text=txt+"\nStaff", width=27, height=11, bg="#FFFDD0", font=("Helventica", 15, "bold"),command=lambda: self.stViewClick(controller)).place(x=580, y=430)
        back = tk.Button(parent, text="BACK", fg="white", bg="red", width=8,height=2,
                             command=lambda: self.stbackclick(controller))
        back.place(x=100, y=750)
