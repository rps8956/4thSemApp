import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('example.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)

#Inserting data
cursor.execute('''INSERT INTO EMPLOYEE
   (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('Ramya', 'Rama priya', 27, 'F', 9000),
   ('Vinay', 'Battacharya', 20, 'M', 6000), 
   ('Sharukh', 'Sheik', 25, 'M', 8300), 
   ('Sarmista', 'Sharma', 26, 'F', 10000),
   ('Tripthi', 'Mishra', 24, 'F', 6000)''')
conn.commit()

#Fetching all the rows before the update
print("Contents of the Employee table: ")
cursor.execute('''SELECT * from EMPLOYEE''')
print(cursor.fetchall())

#Updating the records
sql = '''UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX = 'M' '''
cursor.execute(sql)
print("Table updated...... ")

#Fetching all the rows after the update
print("Contents of the Employee table after the update operation: ")
cursor.execute('''SELECT * from EMPLOYEE''')
print(cursor.fetchall())

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()