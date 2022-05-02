# Establish connection to MySQL database
import mysql.connector
import csv
mydb = mysql.connector.connect(host='localhost',user='root',password='',database='attendence')
print("database connected!")

# Creating cursor object
cursor=mydb.cursor()
data=csv.reader(open('d.csv'))
for row in data:
	cursor.execute("SELECT Sid FROM   attend WHERE  Period IN ('C', 'C++', 'python') GROUP BY Sid HAVING count(*) = 2",row)
	print(row)
# Close database connection

