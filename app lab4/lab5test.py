from tkinter import *
from tkinter.ttk import *
import sqlite3
import tkinter  as tk
from tkinter import messagebox

root = Tk()
root.title("APP_LAB5")
root.geometry("1100x900")

name = StringVar()
lname = StringVar()
email = StringVar()
combo = StringVar()
ad1 = StringVar()
ad2 = StringVar()
ad3 = StringVar()
cmb = StringVar()
phone = IntVar()
ph = IntVar()
hobbies = StringVar()
cn = StringVar()
jt = StringVar()
time = IntVar()
refnm = StringVar()
mob = IntVar()


def data():
    nm = name.get()
    lnm = lname.get()
    eml = email.get()
    com = cmb.get()
    add1 = ad1.get()
    add2 = ad2.get()
    add3 = ad3.get()
    comb = cmb.get()
    phn = phone.get()
    phn1 = ph.get()
    hob = hobbies.get()
    company = cn.get()
    JOB = jt.get()
    tim = time.get()
    nam = refnm.get()
    mobile = mob.get()

    db = sqlite3.connect('JOB.db')
    cursor = db.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS JOB(name TEXT,lname TEXT,email TEXT,combo TEXT,ad1 TEXT,ad2 TEXT,ad3 TEXT,cmb TEXT,phone INT,ph INT,hobbies TEXT,cn TEXT,jt TEXT,time INT,refnm TEXT,mob INT)')
    cursor.execute(
        'INSERT INTO JOB(name,lname,email,combo,ad1,ad2,ad3,cmb,phone,ph,hobbies,cn,jt,time,refnm,mob) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        (nm, lnm, eml, com, add1, add2, add3, comb, phn, phn1, hob, company, JOB, tim, nam, mobile))

    db.commit()
    msg = messagebox.showinfo("DB Demo", "SUBMITTED SUCCESSFULLY")


def display():
    db = sqlite3.connect('JOB.db')
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


ja = Label(root, text="JOB APPLICATION", foreground="black", font=("Arial Bold", 35)).place(x=500, y=0)
pa = Label(root, text="PERSONAL INFORMATION", foreground="red", font=("Arial Bold", 18)).place(x=200, y=70)

name = Label(root, text="NAME:-", font=("Arial", 14)).place(x=200, y=120)
name = Entry(root, width=40)
name.place(x=440, y=125)
lname = Entry(root, width=40)
lname.place(x=700, y=125)

email = Label(root, text="EMAIL:-", font=("Arial", 14)).place(x=200, y=160)
email = Entry(root, width=60)
email.place(x=440, y=160)

edu = Label(root, text="EDUCATION:-", font=("Arial", 14)).place(x=200, y=200)

combo = Combobox(root, text="Please Choose", width=30)
combo['values'] = ("High School", "Senior Secondary Class", "Under Graduate", "Post Graduate")
combo.place(x=440, y=200)

resume = Label(root, text="RESUME:-", font=("Arial", 14)).place(x=200, y=240)
btn = Button(root, text="Choose File").place(x=440, y=240)
chfile = Label(root, text="No choosen File", font=("Arial", 12)).place(x=520, y=240)

add = Label(root, text="ADDRESS:-", font=("Arial", 14)).place(x=200, y=280)

ad1 = Entry(root, width=60)
ad1.place(x=440, y=280)
add1 = Label(root, text="Address 1").place(x=590, y=303)

ad2 = Entry(root, width=60)
ad2.place(x=440, y=330)
add2 = Label(root, text="Address 2").place(x=590, y=353)

ad3 = Entry(root, width=60)
ad3.place(x=440, y=380)
add3 = Label(root, text="Address 3").place(x=590, y=403)

cotr = Label(root, text="COUNTRY:-", font=("Arial", 14)).place(x=200, y=430)

cmb = Combobox(root, text="Choose Country", width=30)
cmb['values'] = (
"India", "Nepal", "Sri Lanka", "Afganistan", "United Kingdom", "United States of America", "Please Text")
cmb.place(x=440, y=430)

phone = Label(root, text="PHONE NUMBER:-", font=("Arial", 14)).place(x=200, y=460)
phone = Entry(root, width=4)
phone.place(x=440, y=460)
ph = Entry(root, width=24)
ph.place(x=490, y=460)

hob = Label(root, text="What are your Hobbies:-", font=("Arial", 14)).place(x=200, y=500)
hobbies = Entry(root, width=120)
hobbies.place(x=200, y=530)

ce = Label(root, text="PREVIOUS/CURRENT EMPLOYMENT DETAILS", foreground="red", font=("Arial Bold", 18)).place(x=200,
                                                                                                                y=560)

cn = Label(root, text="COMPANY NAME:-", font=("Arial", 14)).place(x=200, y=600)
cn = Entry(root, width=30)
cn.place(x=440, y=605)

jt = Label(root, text="JOB TITLE:-", font=("Arial", 14)).place(x=200, y=640)
jt = Entry(root, width=30)
jt.place(x=440, y=640)

time = Label(root, text="HOW LONG WERE YOU HERE?:-", font=("Arial", 14)).place(x=200, y=680)
time = Entry(root)
time.place(x=500, y=680)

ref = Label(root, text="REFERENCE", font=("Arial Bold", 16)).place(x=720, y=605)
refnm = Label(root, text="NAME:-", font=("Arial", 12)).place(x=720, y=640)
refnm = Entry(root, width=40)
refnm.place(x=800, y=640)

mob = Label(root, text="MOB NO.:-", font=("Arial", 12)).place(x=720, y=680)
mob = Entry(root, width=40)
mob.place(x=800, y=680)

msg = Button(root, text='APPLY NOW', command=data, width=20).place(x=400, y=730)

msg = Button(root, text="DISPLAY RECORD(s)", command=display, width=20).place(x=600, y=730)

root.mainloop()