from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import tkinter as tk
from openpyxl import workbook
import openpyxl 
import pathlib
import os
from tkcalendar import *

root = Tk()
root.title("Data Entry")
root.geometry("400x550+460+80")
root.resizable(False,False)






def enter_data():
     firstname = fname_entry.get()
     middlename = mname_entry.get()
     lastname = lname_entry.get()
     email = email_entry.get()
     contact = contact_entry.get()
     age = age_spinbox.get()
     sex = sex_combobox.get()
     yes_no = radio.get()
     birthday = cal.get()
     birthplace = birth_place_entry.get()
     house_number = house_num_entry.get()
     sitio = sitio_combobox.get()
     barangay = barangay_entry.get()
     city = city_entry.get()
     province = province_entry.get()
     botante = voter.get()
     




     #----To have an Error message------
     firstname_error = fname_entry.get()
     middlename_error = mname_entry.get()
     lastname_error = lname_entry.get()
     email_error = email_entry.get()
     contact_error = contact_entry.get()
     age_error = age_spinbox.get()
     sex_error = sex_combobox.get()
     birthplace_error = birth_place_entry.get()
     house_number_error = house_num_entry.get()
     sitio_error = sitio_combobox.get()
     barangay_error = barangay_entry.get()
     city_error = city_entry.get()
     province_error = province_entry.get()
     


     if firstname and middlename and lastname and email and contact and age and sex and yes_no and birthday and birthplace and house_number and sitio and barangay and city and province and botante:
               print("First Name: ", firstname, "Middle Name: ", middlename, "Last Name: ", lastname)
               print("Email:", email, "Contact:", contact)
               print("Age: ", age, "Sex: ",sex, "Are you a PWD?: ", yes_no)
               print("Birthday:", birthday)
               print("Birthplace:", birthplace)
               print("House No.:", house_number, "Sitio:",sitio)
               print("Barangay:",barangay,"City:",city,"Province:",province)
               print("Voter Status:", botante)
               messagebox.showinfo(title="Success", message="Successfully Added People")
     
               filepath = ("C:\\Users\\IVAN\\Documents\\IVAN DOCUMENT\\Python\\Project Barangay\\data.xlsx")
               if not os.path.exists(filepath):
                    workbook = openpyxl.Workbook() 
                    sheet = workbook.active
                    heading = ["First Name", "Middle Name", "Last Name","Email","Contact Number", "Age", "Sex", "Are you a PWD?", "Birthday","Birthplace","House Number", "Sitio", "Barangay","City", "Province","Voter Status"]
                    sheet.append(heading)
                    workbook.save(filepath)
               workbook = openpyxl.load_workbook(filepath)
               sheet = workbook.active
               sheet.append([firstname,middlename,lastname,email,contact,age,sex,yes_no,birthday,birthplace,house_number,sitio,barangay,city,province,botante])
               workbook.save(filepath)
               

               

               

               

     
           
     
          
     

     elif firstname_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your First Name")

     elif middlename_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your Middle Name")
     
     elif lastname_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your Last Name")

     elif email_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your Email")

     elif contact_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your Contact Number")

     elif age_error=="0":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your Age")

     elif sex_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your Gender") 

     elif birthplace_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your Birth Place")

     elif house_number_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your House Number")

     elif sitio_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your Sitio")

     elif barangay_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your Barangay")

     elif city_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your City")

     elif province_error=="":
          messagebox.showerror(title="Please Fill up the Form", message="Please Input your Province")

              
     
          
     




     else:
          print("First Name: ", firstname, "Middle Name: ", middlename, "Last Name: ", lastname)
          print("Email:", email, "Contact:", contact)
          print("Age: ", age, "Sex: ",sex, "Are you a PWD?: ", yes_no)
          print("Birthday:", birthday)
          print("Birthplace:", birthplace)
          print("House No.:", house_number, "Sitio:",sitio)
          print("Barangay:",barangay,"City:",city,"Province:",province)
          print("Voter Status:", botante)
          messagebox.showinfo(title="Success", message="Successfully Added People")
         

def clear():
     fname_entry.delete(0,'end')
     mname_entry.delete(0,'end')
     lname_entry.delete(0,'end')
     email_entry.delete(0,'end')
     contact_entry.delete(0,'end')
     age_spinbox.delete(0,"end")
     sex_combobox.delete(0,"end")
     cal.delete(0, "end")
     birth_place_entry.delete(0, "end")
     house_num_entry.delete(0, "end")
     sitio_combobox.delete(0, "end")

         

def close():
     root.destroy()
     import Information_System   

      


head_label = Label(text="Please fill up this form:", font=("arial", 12,"italic", "bold"))
head_label.place(x=5, y=5)

head_label2 = Label(text="Resident Information of Barangay Dulong Bayan", font=("arial", 12,"italic", "bold"))
head_label2.place(x=10, y=30)


#-------Frame#1------

frame = Frame(root, width=380, height=175, highlightthickness=1, highlightbackground="black")
frame.place(x=10, y=60)

fname_label = Label(frame, text="First Name:", font=("arial", 12))
fname_label.place(x=0, y=5)
fname_entry = Entry(frame, width=10, font=("arial", 10), bd=0, highlightbackground="black", highlightthickness=1)
fname_entry.place(x=110, y=9)

mname_label = Label(frame, text="Middle Name:", font=("arial", 12))
mname_label.place(x=0, y=35)
mname_entry = Entry(frame, width=10, font=("arial", 10), bd=0, highlightbackground="black", highlightthickness=1)
mname_entry.place(x=110, y=37)

lname_label = Label(frame, text="Last Name:", font=("arial", 12))
lname_label.place(x=0, y=65)
lname_entry = Entry(frame, width=10, font=("arial", 10), bd=0, highlightbackground="black", highlightthickness=1)
lname_entry.place(x=110, y=65)

email_label = Label(frame, text="Email:",font=("arial", 12))
email_label.place(x=0, y=95)
email_entry = Entry(frame,width=20, font=("arial", 10), bd=0, highlightbackground="black", highlightthickness=1)
email_entry.place(x=50, y=95)

contact_label = Label(frame, text="Contact No:", font=("arial", 12))
contact_label.place(x=0, y=125)
contact_entry = Entry(frame, width=15, font=("arial", 10), bd=0, highlightbackground="black", highlightthickness=1)
contact_entry.place(x=90,y=125)


age_label = Label(frame, text="Age:", font=("arial", 12))
age_label.place(x=200, y=5)
age_spinbox = Spinbox(frame, from_=0, to=150, bd=0, highlightthickness=1, highlightbackground="black", width=10)
age_spinbox.place(x=240, y=8)

sex_label = Label(frame, text="Sex:", font=("arial", 12))
sex_label.place(x=200, y=45)
sex_combobox = Combobox(frame, values=("Male", "Female"), width=10, font=("arial", 12))
sex_combobox.place(x=240, y=45)

#------radiobutton-----
radio = StringVar()
radio_label = Label(frame, text="Are you a PWD?", font=("arial", 12))
radio_label.place(x=220, y=80)
radio1 = Radiobutton(frame, text="Yes", variable=radio, value="Yes")
radio1.place(x=230, y=100)
radio1.deselect()
radio2 = Radiobutton(frame, text="No", variable=radio, value="No")
radio2.place(x=280, y=100)
radio2.select()





#-----------Frame #2--------------#

frame2 = Frame(root, width=380, height=287, highlightbackground="black", highlightthickness=1)
frame2.place(x=10, y=240)

birthday_label = Label(frame2, text="Birthday:", font=("arial", 12))
birthday_label.place(x=0, y=2)
cal = DateEntry(frame2, setmode="day", date_pattern="mm/dd/yyyy", font=("arial", 10))
cal.place(x=80, y=3)



birth_place = Label(frame2, text="Birthplace:",font=("arial", 12))
birth_place.place(x=0, y=33)
birth_place_entry = Entry(frame2,width=20,font=("arial", 12), highlightthickness=1, highlightbackground="black")
birth_place_entry.place(x=80,y=33)


house_num = Label(frame2,text="House no.:", font=("arial", 12))
house_num.place(x=0, y=63)
house_num_entry = Entry(frame2, width=10,font=("arial", 12), highlightthickness=1, highlightbackground="black")
house_num_entry.place(x=80, y=63)

sitio_label = Label(frame2,text="Sitio:", font=("arial", 12))
sitio_label.place(x=0, y=93)
sitio_combobox = Combobox(frame2, values=("Central", "Himpot", "Talisay","Annapolis", "Samantha", "Concordia", "Linawan", "Lote","Puyat", "Ibabaw","Morning Glory"), width=15, font=("arial", 12))
sitio_combobox.place(x=80, y=93)


barangay_label = Label(frame2, text="Barangay:",font=("arial", 12))
barangay_label.place(x=0, y=123)
barangay_entry = Entry(frame2, width=20,font=("arial", 12), highlightthickness=1, highlightbackground="black")
barangay_entry.place(x=80, y=123)
barangay_entry.insert(0,"Dulong Bayan")

city_label = Label(frame2,text="City:", font=("arial", 12))
city_label.place(x=0, y=153)
city_entry = Entry(frame2, width=20,font=("arial", 12), highlightthickness=1, highlightbackground="black")
city_entry.place(x=80, y=153)
city_entry.insert(0, "San Jose Del Monte")


province_label = Label(frame2,text="Province:", font=("arial", 12))
province_label.place(x=0, y=183)
province_entry = Entry(frame2, width=20, font=("arial", 12), highlightthickness=1, highlightbackground="black")
province_entry.place(x=80, y=183)
province_entry.insert(0, "Bulacan")

voter = StringVar(value="Not a Voter")
voters_check = Checkbutton(frame2, text="Are you a voter? (If not don't check)", font=("arial", 12), variable=voter, onvalue="Voter", offvalue="Not a Voter")
voters_check.place(x=0, y=213)


addbtn = Button(root, text="Add People", font=("arial", 12), command= enter_data)
addbtn.place(x=50 , y=490)





clearbtn = Button(root, text="Clear", font=("arial", 12), command= clear)
clearbtn.place(x=170, y=490)


backbtn = Button(root, text="Back", font=("arial", 12), command= close)
backbtn.place(x=250 , y=490)



root.mainloop()