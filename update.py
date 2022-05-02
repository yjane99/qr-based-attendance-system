# Import required modules
import csv
import sqlite3

# Connecting to the geeks database
connection = sqlite3.connect('Student_Attendence.db')

print("Opened database successfully")

cursor = connection.cursor()

file = open('d.csv')
 
# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)
 
# SQL query to insert data into the
# person table
insert_records = "INSERT INTO attendence (Sid,branch,Sec,Year,Period,Time,Date) VALUES(?, ?,?, ?, ?, ?, ?)"
 
# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, contents)
 
# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM attendence"
rows = cursor.execute(select_all).fetchall()
 
# Output to the console screen
for r in rows:
    print(r)
 
# Committing the changes
connection.commit()

connection.close()

