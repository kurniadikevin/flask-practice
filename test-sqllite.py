#!/usr/bin/python

import sqlite3

#connect to database test.db , if there is none then it created one
conn = sqlite3.connect('test.db')

print ("Opened database successfully")

# create new table ----------------->
""" conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully") """

#------BASIC CRUD------------>

#-------CREATE ----insert data to conn test.db--------------->
""" conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print ("Records created successfully") """

#------ READ ------ Select data and display each on-->
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print (f"ID =  {row[0]}")
   print (f"NAME = {row[1]}")
   print (f"ADDRESS = {row[2]}")
   print (f"SALARY = {row[3]}\n")

print ("Operation done successfully")

#------UPDATE ----- Update data-->
""" conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print (f"Total number of rows updated : {conn.total_changes}")
 """

#----DELETE ---- delete data -->
""" conn.execute("DELETE from COMPANY where ID = 3")
conn.commit()
print (f"Total number of rows deleted : {conn.total_changes}") """


conn.close()