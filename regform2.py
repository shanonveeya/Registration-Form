from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   con = sqlite3.connect('Form.db')
   with con:
      cursor=con.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
   con.commit()
   
   
             
label_0 = Label(root, text="Registration form",width=20,font=("times new roman", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Full Name",width=20,font=("times new roman", 10))
label_1.place(x=78,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("times new roman", 10))
label_2.place(x=65,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("times new roman", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Country",width=20,font=("times new roman", 10))
label_4.place(x=71,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=16)
c.set('Select Your Country') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Programming",width=20,font=("times new roman", 10))
label_4.place(x=85,y=330)
var2= IntVar()
var3=IntVar()
Checkbutton(root, text="Java", variable=var1).place(x=235,y=330)

Checkbutton(root, text="Python", variable=var2).place(x=290,y=330)

Checkbutton(root, text="C++", variable=var3).place(x=360,y=330)

Button(root, text='Submit',width=20,bg='black',fg='white',command=database).place(x=200,y=380)

root.mainloop()
