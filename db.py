import mysql.connector
from mysql import connector
import csv
from flask import Flask, render_template, request,session,redirect,flash,url_for

app = Flask(__name__,template_folder='templates')



@app.route('/home')
def Home():
    mydb = mysql.connector.connect(host='localhost',user='root',password='',database='attendence')
    print("database connected!")
    cursor=mydb.cursor()
    data=csv.reader(open('d.csv'))
    for row in data:
        cursor.execute('INSERT INTO attend (Sid,branch,Sec,Year,Period,Time) VALUES(%s,%s,%s,%s,%s,%s)',row)
    print(row)
    
    mydb.commit()
    cursor.close()
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)