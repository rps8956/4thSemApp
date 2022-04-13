from tkinter import *
import sqlite3
import tkinter  as tk
from tkinter import messagebox

window = Tk()
window.geometry("1100x900")

cash = IntVar()
deb = IntVar()
cred = IntVar()
oth = IntVar()


def Database():
    cs = cash.get()
    tx = deb.get()
    ttl = cred.get()
    amount = oth.get()

    db = sqlite3.connect('vehc.db')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS VEHC(cash INT,deb INT,cred INT,oth INT)')
    cursor.execute('INSERT INTO VEHC(cash,deb,cred,oth) VALUES(?,?,?,?)', (cs, tx, ttl, amount))
    db.commit()
    msg = messagebox.showinfo("DB Demo", "WELCOME")


def display():
    db = sqlite3.connect('vehc.db')
    with db:
        cursor = db.cursor()
        my_w = tk.Tk()
        my_w.geometry("400x250")

        r_set = cursor.execute('''SELECT * from VEHC ''');
        i = 0
        for VEHC in r_set:
            for j in range(len(VEHC)):
                e = Entry(my_w, width=10, fg='black')
                e.grid(row=i, column=j)
                e.insert(END, VEHC[j])
            i = i + 1


cash = Entry(window)
cash.place(x=200, y=23)
deb = Entry(window)
deb.place(x=200, y=43)
cred = Entry(window)
cred.place(x=200, y=63)
oth = Entry(window)
oth.place(x=200, y=83)

a = Checkbutton(window, text="CASH:-", font=("Calibri", 12)).place(x=100, y=20)
b = Checkbutton(window, text="DEBIT:-", font=("Calibri", 12)).place(x=100, y=40)
c = Checkbutton(window, text="CREDIT:-", font=("Calibri", 12)).place(x=100, y=60)
d = Checkbutton(window, text="OTHER:-", font=("Calibri", 12)).place(x=100, y=80)

msg = Button(window, text='SUBMIT', command=Database, width=20).place(x=400, y=200)
msg = Button(window, text="DISPLAY RECORD(s)", command=display, width=20).place(x=600, y=200)

window.mainloop()  # closed

import sqlite3

my_conn = sqlite3.connect('vehc.db')

import tkinter  as tk
from tkinter import *

my_w = tk.Tk()
my_w.geometry("1300x250")

r_set = my_conn.execute('''SELECT * from VEHC ''');
i = 0  # row value inside the loop
for VEHC in r_set:
    for j in range(len(VEHC)):
        e = Entry(my_w, width=10, fg='black')
        e.grid(row=i, column=j)
        e.insert(END, VEHC[j])
    i = i + 1
my_w.mainloop()
