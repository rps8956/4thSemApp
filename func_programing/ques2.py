from tkinter import *
from tkinter.ttk import *
import sqlite3
import tkinter  as tk
from tkinter import messagebox

root = Tk()
root.title("APP UPE")
root.geometry("1100x900")

name = StringVar()
m_name = StringVar()
classs = StringVar()
b_id = IntVar()
sh_time= IntVar()
no_tickets = IntVar()

def data():
    nm = name.get()
    mnm = m_name.get()
    cls = classs.get()
    bid = b_id.get()
    ntick= no_tickets.get()
    sht = sh_time.get()

    db = sqlite3.connect('app_upe.db')
    cursor = db.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS JOB(name TEXT,m_name TEXT,classs TEXT,b_id INT,no_tickets INT,sh_time INT)')
    cursor.execute(
        'INSERT INTO JOB(b_id,name,m_name,classs,no_tickets,sh_time) VALUES(?,?,?,?,?,?)',
        (nm, mnm, cls, bid, ntick, sht))

    db.commit()

    msg = messagebox.showinfo("DB Demo", "SUBMITTED SUCCESSFULLY")
    # clear the text boxes
    name.delete(0, END)
    m_name.delete(0, END)
    #classs.delete(0, END)
    b_id.delete(0, END)
    #no_tickets.delete(0, END)
    #sh_time.delete(0, END)

def display():
    db = sqlite3.connect('app_upe.db')
    with db:
        cursor = db.cursor()
        my_w = Tk()
        my_w.geometry("400x250")

        r_set = cursor.execute('''SELECT * from JOB ''');
        i = 0
        for JOB in r_set:
            for j in range(len(JOB)):
                e = Entry(my_w, width=10)
                e.grid(row=i, column=j)
                e.insert(END, JOB[j])
            i = i + 1

b_id = Label(root, text="Booking ID:-", font=("Arial", 14)).place(x=200, y=120)
b_id = Entry(root, width=40)
b_id.place(x=440, y=125)

na = Label(root, text="Person Name:-", font=("Arial", 14)).place(x=200, y=160)
name = Entry(root, width=60)
name.place(x=440, y=160)

m_name = Label(root, text="Movie Name:-", font=("Arial", 14)).place(x=200, y=200)
m_name = Entry(root, width=60)
m_name.place(x=440, y=200)

cla = Label(root, text="Class:-", font=("Arial", 14)).place(x=200, y=240)

R1 = Radiobutton(root, text="A", variable=classs, value="A").place(x=280,y=240)
R2 = Radiobutton(root, text="B", variable=classs, value="B").place(x=320,y=240)

C1 = Checkbutton(root, text = "7:15", variable = sh_time, \
                 onvalue = 1, offvalue = 0,\
                 width = 20).place(x=360,y=240)
no_tickes = Label(root, text="No of Tickets:-", font=("Arial", 14)).place(x=200, y=280)
combo = Combobox(root, text="Please Choose", width=30)
combo['values'] = ("1", "2", "3", "4")
combo.place(x=360, y=280)

msg = Button(root, text='INSERT', command=data, width=20).place(x=220, y=350)
msg = Button(root, text='UPDATE', command=data, width=20).place(x=340, y=350)
msg = Button(root, text='DELETE', command=data, width=20).place(x=220, y=400)
msg = Button(root, text='SELECT', command=display, width=20).place(x=340, y=400)

root.mainloop()








