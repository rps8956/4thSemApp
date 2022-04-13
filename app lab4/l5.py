from  tkinter import *
import sqlite3
root = Tk()
root.geometry("412x717")
root.title('JOB Application')

# Create a database or connect to one
conn = sqlite3.connect('application_book.db')

#create cursor
c = conn.cursor()

#create table
c.execute("""CREATE TABLE application(
first_name text,
last_name text,
email text,
education text,
resume text,
address text,
country text,
city text,
state text,
zip integer,
phone integer,
hobbies text,
company text,
JOB text,
years integer,
n1 text,
p1 integer,
n2 text,
p2 integer

)""")

#submit func
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('application_book.db')
    # create cursor
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address)",
              {
                  'f_name':f_name.get(),
                  'l_name':l_name.get(),
                  'address':address.get()
              }


              )


    # commit changes
    conn.commit()
    # close connections
    conn.close()

label = Label(root,text="",bg = "maroon").pack(side="top",fill = "x")

label_0 =Label(root,text="JOB Application", width=20,font=("bold",20))
label_0.place(x=90,y=20)
label = Label(root,text="Personal information",fg='maroon',font = ("bold",15))
label.place(x=10,y=60)

label_1 =Label(root,text="Name", font=("bold",10))
label_1.place(x=10,y=90)

name=Entry(root)
name.place(x=120,y=90)
entry99 = Entry(root)
entry99.place(x=260,y=90)

label71 = Label(root,text="First Name",font=("bold",5))
label71.place(x=140,y=107)

label70 = Label(root,text="Last Name",font=("bold",5))
label70.place(x=280,y=107)

label_3 =Label(root,text="Email",font=("bold",10))
label_3.place(x=10,y=120)

email=Entry(root,fg="grey")
email.insert(0,"user@example.com")
email.place(x=120,y=120)

label_5=Label(root,text="Education",font=("bold",10))
label_5.place(x=10,y=150)

list_of_country=[ 'Undergraduate' ,'Postgraduate' , 'High school' ,'12th']

c=StringVar()
droplist=OptionMenu(root,c, *list_of_country)
droplist.config(width=15,bg="white")
c.set('Please Choose')
droplist.place(x=120,y=150)

label_98 =Label(root,text="Resume",font=("bold",10))
label_98.place(x=10,y=180)


ad1=Entry(root,fg="grey",font=("light",10))
ad1.insert(0,"                        No file chosen")
ad1.place(x=120,y=180,width= 330)
choose_files = Button(root,text="Choose file")
choose_files.place(x=130,y=183,height=13)

label_97 =Label(root,text="Address",font=("bold",10))
label_97.place(x=10,y=210)

ad2=Entry(root)
ad2.place(x=120,y=210,width= 330)

label50 = Label(root,text="Address 1",font=("bold",5))
label50.place(x=250,y=227)


entry_96=Entry(root)

entry_96.place(x=120,y=240,width= 330)
label51 = Label(root,text="Address 2",font=("bold",5))
label51.place(x=250,y=257)

list_of_country=[ 'Australia' ,'India' , 'United States' ,'United Kingdom']

d=StringVar()
droplist=OptionMenu(root,d, *list_of_country)
droplist.config(width=50)
d.set('Select a country                                                                        ')
droplist.place(x=120,y=267)

entry_94 = Entry(root)
entry_94.place(x=120,y=300,width=160)

label49 = Label(root,text="City",font=("bold",5))
label49.place(x=184,y=317)

entry_93 = Entry(root)
entry_93.place(x=285,y=300,width=70)

label48 = Label(root,text="State",font=("bold",5))
label48.place(x=310,y=317)

entry_92 = Entry(root)
entry_92.place(x=360,y=300,width=100)

label48 = Label(root,text="Zip Code",font=("bold",5))
label48.place(x=380,y=317)

label = Label(root,text="Phone Number",font=("bold",10))
label.place(x=10,y=330)
entry = Entry(root)
entry.place(x=120,y=330,width=30)
entry91 = Entry(root)
entry91.place(x=155,y=330,width=320)
label90 = Label(root,text="What are your hobbies?",font=("bold",10))
label90.place(x=10,y=360)
entry90 =Entry(root)
entry90.place(x=10,y=380,width=500)

label89 = Label(root,text="Previous/Current Employment Details",fg="maroon",font=("bold",15))
label89.place(x=10,y=410)

label88 = Label(root,text="Company Name",font=("bold",10))
label88.place(x=10,y=440)
entry88 = Entry(root)
entry88.place(x=120,y=440,width=350)

label87 = Label(root,text="JOB Title",font=("bold",10))
label87.place(x=10,y=470)
entry87 = Entry(root)
entry87.place(x=120,y=470,width=330)

label86 = Label(root,text="How long were you\nhere?",font=("bold",10))
label86.place(x=5,y=510)
entry86 = Entry(root)
entry86.place(x=120,y=510,width=350)

label85 = Label(root,text="Referance#1",fg="maroon",font=("bold",15))
label85.place(x=10,y=550)

label84 = Label(root,text="Name",font=("bold",10))
label84.place(x=10,y=580)
entry84 = Entry(root)
entry84.place(x=120,y=580,width=350)

label83 = Label(root,text="Phone",font=("bold",10))
label83.place(x=10,y=610)
entry83 = Entry(root)
entry83.place(x=120,y=610,width=350)

label82 = Label(root,text="Referance#2",fg="maroon",font=("bold",15))
label82.place(x=10,y=640)

label81 = Label(root,text="Name",font=("bold",10))
label81.place(x=10,y=670)
entry81 = Entry(root)
entry81.place(x=120,y=670,width=350)

label80 = Label(root,text="Phone",font=("bold",10))
label80.place(x=10,y=700)
entry80 = Entry(root)
entry80.place(x=120,y=700,width=350)

Button(root, text='Apply' , width=20,bg="maroon",fg='white').place(x=180,y=740)
root.mainloop()