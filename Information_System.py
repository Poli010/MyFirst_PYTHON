from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import openpyxl
import os
import subprocess



   

root = Tk()
root.title("Information System")
root.geometry("750x500+260+100")
root.config(bg="#333333")
root.resizable(False,False)


def load_data():
    path = "C:\\Users\\IVAN\\Documents\\IVAN DOCUMENT\\Python\\Project Barangay\\data.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    list_values = list(sheet.values)
    cols = list_values[0]
    tree = ttk.Treeview(frame, column= cols, show="headings")
    for col_name in cols:
        tree.heading(col_name, text = col_name)
    tree.pack()
    
    for value_tuple in list_values[1:]:
        tree.insert('',END, values=value_tuple)

def open_excel():
    os.startfile("C:\\Users\\IVAN\\Documents\\IVAN DOCUMENT\\Python\\Project Barangay\\data.xlsx")

def add_resident():
    root.destroy()
    import data_entry
    
    

def close():
    root.destroy()
    import login    

Head_lbl = Label(text="Barangay Dulong Bayan ", font=("arial",18,"bold"), fg="White", bg="#333333")
Head_lbl.place(x=230, y=10)   
Head_lbl2 = Label(text=" Resident Information System", font=("arial",18,"bold"), fg="White", bg="#333333")
Head_lbl2.place(x=180, y=50) 


db_logo = PhotoImage(file="C:\\Users\\IVAN\\Documents\\IVAN DOCUMENT\\Python\\Project Barangay\\pictures\\dulong_bayan2.png")
sjdm_logo = PhotoImage(file="C:\\Users\\IVAN\\Documents\\IVAN DOCUMENT\\Python\\Project Barangay\\pictures\\San jose del monte.png")

db = Label(root, image=db_logo, bg="#333333")
db.place(x=10, y=0)

sjdm = Label(root, image=sjdm_logo, bg="#333333")
sjdm.place(x=640, y=0)
#--------#-----------#



frame = Frame(root, bg="#ffffff", width=700, height=300)
frame.place(x=0, y=140)


load_data()

open = Button(root, text="Edit", width=15, command= open_excel)
open.place(x=50, y=400)

add = Button(root, text="Add Resident", width=15, command= add_resident)
add.place(x=300, y=400)

logout = Button(root, text="Logout", width=15, command= close)
logout.place(x=600, y=400)

root.mainloop()