'''
Restaurant management page
'''
import tkinter as tk
from PIL import ImageTk

class Restaurant(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, stick="nsew")
        self.bg = ImageTk.PhotoImage(file="images/im2.jpeg")
        self.bg_img = tk.Label(self, image=self.bg)
        self.bg_img.place(x=0, y=0, relwidth=1, relheight=1)
        ins_res=Res_Fram(self,controller,"Insert")
        ins_res.place(x=170, y=70, height=300, width=350)
        upd_res=Res_Fram(self,controller,"Update")
        upd_res.place(x=570, y=70, height=300, width=350)
        del_res=Res_Fram(self,controller,"Delete")
        del_res.place(x=170, y=420, height=300, width=350)
        view=Res_Fram(self,controller,"View")
        view.place(x=570, y=420, height=300, width=350)

class Res_Fram(tk.Frame):
    def rsviewclick(self,controller):
        controller.show_frame("RV")
    def rsbackclick(self,controller):
        controller.show_frame("H")
    def rsupdclick(self,controller):
        controller.show_frame("RU")
    def rsinsclick(self,controller):
        controller.show_frame("RI")
    def rsdelclick(self,controller):
        controller.show_frame("RD")
    def __init__(self,parent,controller,txt):
        tk.Frame.__init__(self, parent, bg="#FFFDD0", highlightbackground="black", highlightthickness=5)
        if txt == "Insert":
            B = tk.Button(parent, text=txt + "\nItem", width=27, height=11, bg="#FFFDD0",
                          font=("Helventica", 15, "bold"),command=lambda: self.rsinsclick(controller)).place(x=180, y=80)
        elif txt == "Update":
            B = tk.Button(parent, text=txt + "\nItem", width=27, height=11, bg="#FFFDD0",
                          font=("Helventica", 15, "bold"),command=lambda: self.rsupdclick(controller)).place(x=580, y=80)
        elif txt == "Delete":
            B = tk.Button(parent, text=txt + "\nItem", width=27, height=11, bg="#FFFDD0",
                          font=("Helventica", 15, "bold"),command=lambda: self.rsdelclick(controller)).place(x=180, y=430)
        elif txt=="View":
            B=tk.Button(parent, text=txt+"\nItem", width=27, height=11, bg="#FFFDD0", font=("Helventica", 15, "bold"),command=lambda: self.rsviewclick(controller)).place(x=580,y=430)
        back = tk.Button(parent, text="BACK", fg="white", bg="red", width=8,height=2,
                             command=lambda: self.rsbackclick(controller))
        back.place(x=100, y=750)
