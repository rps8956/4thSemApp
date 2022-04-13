
from tkinter import *
import sqlite3
root = Tk()
root.geometry("500x500")
root.title("Practising SQL")
# Create a database or connect to one
conn = sqlite3.connect('address_book.db')


#create cursor
c = conn.cursor()

#create table
# c.execute("""CREATE TABLE addresses(
# first_name text,
# last_name text,
# city text
# )""")

#submit func
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
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



    #clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
def query():
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    q_label = Label(root,text = print_records)
    q_label.grid(row = 11,column=0)


    # commit changes
    conn.commit()
    # close connections
    conn.close()



f_name = Entry(root,width=30)
f_name.grid(row=0,column=1)
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)
address = Entry(root,width=30)
address.grid(row=2,column=1)

sub_btn = Button(root,text="Add entry to the database",command=submit)
sub_btn.grid(row=4,column=0)

#query botton
query_button = Button(root,text="Show records",command=query)
query_button.grid(row=9,column=0)

#commit changes
conn.commit()


#close connections
conn.close()
root.mainloop()

