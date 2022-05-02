from distutils.log import debug
from unittest import result
import mysql.connector
from flask import Flask, Markup, render_template
import mysql.connector
import numpy as np
app = Flask(__name__,template_folder='templates')


def Display():
    conn = mysql.connector.connect(user='root',host='localhost',password ='',database='attendence')
    mycursor = conn.cursor()
    sql = '''SELECT COUNT(*) Period FROM attend where Sid="b'Co5617'"'''
    mycursor.execute(sql)
    myresult = mycursor.fetchone()[0]
    conn.close()
    return myresult

def Count():
    conn = mysql.connector.connect(user='root',host='localhost',password ='',database='attendence')
    mycursor = conn.cursor()
    sql = 'SELECT Sid,COUNT(Sid) FROM attend GROUP BY  Sid ORDER BY COUNT(Sid) DESC' ;
    mycursor.execute(sql)
    result = mycursor.fetchall()
    conn.close()
    return result



@app.route('/display.html')
def index():
    myresult = Display()
    result = Count()
    return render_template('display.html',myresult=myresult,result=result)
if __name__ == '__main__':
    app.run(debug=True)



