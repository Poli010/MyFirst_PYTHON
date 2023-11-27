from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Login")
root.geometry("750x500+260+100")
root.configure(background="#333333")
root.resizable(False, False)

#creating widgets
image = ImageTk.PhotoImage(Image.open("C:\\Users\\IVAN\\Documents\\IVAN DOCUMENT\\Python\\tkinter\\pictures\\eyy.jpg"))
img = Label(image=image, background="#333333", width=300, height=300)
frame = Frame(root, width=300, height=300, background="#333333")
heading = Label(frame, text="Sign in", background="#333333",fg="White", font=("Eras Demi ITC", 14, "italic"))
username_entry = Entry(frame, width=25, fg="White", border=0, background="#333333", font=("Eras Demi ITC", 12))
password_entry = Entry(frame, width=25, fg="White", border=0, background="#333333", font=("Eras Demi ITC", 12))





#username and password auto delete when typing 
def user_enter(u):
 username_entry.delete(0, "end")

def user_leave(u):
    if username_entry.get()=="":
     username_entry.insert(0, "Username")
    

def pass_enter(p):
 password_entry.delete(0, "end")

def pass_leave(p):
    if password_entry.get()=="":
     password_entry.insert(0, "Password")





#username entry and password entry function that when enter, automatically remove the username and password label
button_mode = True
def hide():
    global button_mode
    if button_mode:
        closebutton.config(image=closeeye, activebackground="White")
        password_entry.config(show="*")
        button_mode=False
    
    else:
        eyebutton.config(image=openeye, activebackground="White")
        password_entry.config(show="")
        button_mode = True





# sign in button function
def open():
 username_server ="Admin"
 password_server = "Admin123"
 if username_entry.get()==username_server and password_entry.get()==password_server:
    messagebox.showinfo(title="Welcome",message="Successfully Login")
    root.destroy() 
    import Information_System
    
    
 else:
    messagebox.showerror(title="Error", message="Invalid Username or Password")







#buttons
openeye = PhotoImage(file="C:\\Users\\IVAN\\Documents\\IVAN DOCUMENT\\Python\\tkinter\\pictures\\openeye.png")
closeeye = PhotoImage(file="C:\\Users\\IVAN\\Documents\\IVAN DOCUMENT\\Python\\tkinter\\pictures\\closeye.png")
eyebutton = Button(frame, image=openeye, bg="#333333",border=0, command=hide)
closebutton = Button(frame, image=closeeye, bg="#333333",border=0, command=hide)
signinbutton = Button(frame, width=25, pady=5, border=0, text="Sign in", bg="#57a1f8", fg="White", command=open)





#show widgets on the screen
img.place(x=50, y=100)
frame.place(x=370, y=100)
heading.place(x=135, y=0)
username_entry.place(x=30, y=80)
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", user_enter)
username_entry.bind("<FocusOut>", user_leave)
password_entry.place(x=30, y=130)
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", pass_enter)
password_entry.bind("<FocusOut>", pass_leave)
eyebutton.place(x=270, y=125)
signinbutton.place(x=70, y=180)





#line on frame
line = Frame(frame, width=295, height=1, bg="white")
line.place(x=25, y=110)
line2 = Frame(frame, width=295, height=1, bg="white")
line2.place(x=25, y=160)











root.mainloop()