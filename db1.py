import mysql.connector
import csv
mydb = mysql.connector.connect(host='localhost',user='root',password='',database='attendence')
print("database connected!")
cursor=mydb.cursor()
data=csv.reader(open('d.csv'))
for row in data:
    cursor.execute('INSERT INTO attend (Sid,branch,Sec,Year,Period,Time,Date) VALUES(%s,%s,%s,%s,%s,%s,%s)',row)
    print(row)
    
mydb.commit()
cursor.close()


def Count():
    conn = mysql.connector.connect(user='root',host='localhost',password ='',database='attendence')
    mycursor = conn.cursor()
    sql = 'SELECT Sid,COUNT(Sid) FROM attend GROUP BY  Sid ORDER BY COUNT(Sid) DESC' ;
    mycursor.execute(sql)
    result = mycursor.fetchall()
    conn.close()
    return result

result = Count()

    


