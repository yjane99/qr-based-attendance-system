from pickle import NONE
from flask import Flask, render_template, request,session,redirect,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
from datetime import datetime
import json
from flask_mysqldb import MySQL
import pandas as pd
import pyqrcode
from MyQR import myqr
import os
from promise import Promise
import mysql.connector  as sql_db 


import time
from datetime import datetime


#from tkinter import *
from threading import Thread
from PIL import ImageTk, Image
from flask import Flask, jsonify, request
import numpy as np
from mysql import connector
import csv
from flask_mysqldb import MySQL

import MySQLdb.cursors
import re
from dotenv import load_dotenv

# loading environment variables
load_dotenv()

labels = [
    'Java','Pyhton','C','C++','m1','m2'
]


values = [3.3,6.66,10,13.33,16.66,0,20,23.33,
26.33,30,33.33,36.66,40,43.33,46.66,50,53.33,56.66,60,
63.33,66.66,70,73.33,76.66,80,
83.33,86.66,90,93.33,96.66,100]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__,template_folder='templates')
app.secret_key = 'super-secret-key'


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['ENV'] = 'development'
app.config['DEBUG'] = False
app.config['TESTING'] = False
app.config['MAIL_USERNAME'] = os.getenv('SMTP_MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('SMTP_MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'attendence'

mysql = MySQL(app)

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.JSON, nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    cpassword = db.Column(db.String(10), nullable=False)


class Attend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Sid = db.Column(db.String(50), nullable=False)
    Sname=db.Column(db.String(50), nullable=False)
    Semail = db.Column(db.String(50), nullable=False)
    Temail=db.Column(db.String(50), nullable=False)
    branch = db.Column(db.String(50), nullable=False)
    Subject = db.Column(db.String(50), nullable=False)
    Year =  db.Column(db.String(50), nullable=False)
    Status = db.Column(db.String(10), nullable=False)
    Time = db.Column(db.String(50), nullable=False)
    Date = db.Column(db.String(50), nullable=False)
    QRtime=db.Column(db.String(100), nullable=False)

class Student_query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Integer, primary_key=True)

class Sregister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    uname = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.Integer(), nullable=False)
    email =  db.Column(db.String(50), nullable=False)
    year =  db.Column(db.String(50), nullable=False)
    branch =  db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    cpassword = db.Column(db.String(10), nullable=False)

class Pregister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    uname = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    email =  db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    cpassword = db.Column(db.String(10), nullable=False)

class Pcontact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    child_name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    subject =db.Column(db.String(50),nullable=False)
    message=db.Column(db.String(50),nullable=False) 

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    subject=db.Column(db.String(50),nullable=False)
    message=db.Column(db.String(250),nullable=False)

def send_mail(email_f):
    email=email_f['email']
    file_name=email_f['file']
    try:
        subject="Attendance QR Code for lecture"
        msg = Message(subject, sender = os.getenv('SMTP_MAIL_USERNAME'), recipients = [email])
        msg.body = '''Dear Student, Your QR code for the lecture is attached herewith, this QR code is valid only for 35 minutes.'''
        with app.open_resource(os.getcwd() + "\\" + file_name) as fp:  
            msg.attach(file_name,"image/png",fp.read())  
        mail.send(msg)
        print("Email sent")
        
    except Exception as e:
        print('Error: {}'.format(e))
        print('\nEmail failed to send!')

def decode_binary(binary_list):
    st=binary_list.decode()
    res = st.strip('][').split(', ')
    temp=[]
    for i in res:
        temp.append(i.strip('""'))

    return temp

def mark_attendance(Sid,Time):
    ts=time.time()
    append_ts=int(ts)
    if append_ts-int(Time) < 2100:
        print("valid......................")
        conn = sql_db.connect(user='root',host='localhost',password ='',database='attendence')
        mycursor = conn.cursor()
        sql = 'UPDATE attend SET Status= %s WHERE Sid= %s AND QRtime= %s'
        tuple=("P",Sid,Time)
        mycursor.execute(sql,tuple)
        conn.commit()
        conn.close()
        return "1"
    else:
        print("invalid..........")
        return "0"

def fetch_user_info(Sid):
    conn = sql_db.connect(user='root',host='localhost',password ='',database='attendence')
    mycursor = conn.cursor()
    sql = 'SELECT *FROM sregister WHERE Sid= %s'
    tuple=(Sid,)
    mycursor.execute(sql,tuple)
    sub_result = mycursor.fetchone()
    conn.close()
    return sub_result
    






@app.route('/update-file/', methods=['POST','GET'])
def lets_try():
    try:
        # geting the json request
        jsonValue = request.get_json()
        jsonData = jsonValue['decodedText']
        SidandTime = jsonData.split(" ")
        print(SidandTime)
        get_response=mark_attendance(SidandTime[0],SidandTime[1])
        user_data = fetch_user_info(SidandTime[0])

        return {"success":get_response,"data":user_data}
    except Exception as error:
        
        return {"success":"error","data":[]}

@app.route("/")
def Home():
    return render_template('index.html',params=params)

@app.route("/about.html")
def About():
    return render_template('about.html',params=params)

@app.route("/login.html",methods=['GET','POST'])
def Login():
    if (request.method== "GET"):
        if('email' in session and session['email']):
            return render_template('Teacher_dashboard.html',params=params)
        else:
            return render_template("login.html", params=params)

    if (request.method== "POST"):
        email = request.form.get('email')
        password = request.form["password"]
        
        login = Register.query.filter_by(email=email, password=password).first()
        if login is not None:
            session['email']=email
            return render_template('Teacher_dashboard.html',params=params)
        else:
            flash("plz enter right password",'error')
            return render_template('login.html',params=params)



@app.route("/register.html", methods=['GET','POST'])
def tregister():
    if(request.method=='POST'):
        name = request.form.get('name')
        subject = request.form.getlist('subject')
        mobile = request.form.get('mobile')
        email= request.form.get('email')
        password= request.form.get('password')
        cpassword= request.form.get('cpassword')
        print(password)

        user=Register.query.filter_by(email=email).first()
        if user:
            flash('Account already exist!Please login','success')
            return redirect(url_for('register'))
        if not(len(name)) >3:
            flash('length of name is invalid','error')
            return redirect(url_for('register.html')) 
        if (len(mobile))<10:
            flash('invalid mobile number','error')
            return redirect(url_for('register.html')) 
        if (len(password))<8:
            flash('length of password should be greater than 7','error')
            return redirect(url_for('register.html'))
        else:
             flash('You have registered successfully','success')
            
        entry = Register(name=name,subject=subject,mobile=mobile,email=email,password=password,cpassword=cpassword)
        db.session.add(entry)
        db.session.commit()
    return render_template('register.html',params=params)


@app.route("/sregister.html", methods=['GET','POST'])
def sregister():
    if(request.method=='POST'):
        sid = request.form.get('sid')
        name = request.form.get('name')
        uname = request.form.get('uname')
        mobile = request.form.get('mobile')
        email= request.form.get('email')
        year = request.form.get('year')
        branch = request.form.get('branch')
        password= request.form.get('password')
        cpassword= request.form.get('cpassword')
        file1 = open("students.txt", "a")
        file1.write("\n")  # append mode
        file1.write(sid)
        file1.close()


        user=Sregister.query.filter_by(email=email).first()
        if user:
            flash('Account already exist!Please login','success')
            return redirect(url_for('sregister'))
        if not(len(name)) >3:
            flash('length of name is invalid','error')
            return redirect(url_for('sregister')) 
         
        if (len(password))<8:
            flash('length of password should be greater than 7','error')
            return redirect(url_for('sregister'))
        else:
             flash('You have registtered succesfully','success')
            
        entry = Sregister(sid=sid,name=name,mobile=mobile,uname=uname,email=email,year=year,branch=branch,password=password,cpassword=cpassword)
    
        db.session.add(entry)
        db.session.commit()
    return render_template('sregister.html',params=params)

@app.route('/slogin.html', methods =['GET', 'POST'])
def slogin():
    msg = ''
    if request.method == 'POST'  and 'email' in request.form and 'password' in request.form and 'Sid' in request.form:

        Sid = request.form['Sid']
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM sregister WHERE Sid = %s AND email = % s AND password = % s', (Sid, email, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['Sid'] = account['Sid']
            session['email'] = account['email']
            msg = 'Logged in successfully !'
            return render_template('student_dashboard.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('slogin.html', msg = msg)

@app.route("/pregister.html", methods=['GET','POST'])
def pregister():
    if(request.method=='POST'):
        name = request.form.get('name')
        uname = request.form.get('uname')
        mobile = request.form.get('mobile')
        email= request.form.get('email')
        password= request.form.get('password')
        cpassword= request.form.get('cpassword')

        user=Pregister.query.filter_by(email=email).first()
        if user:
            flash('Account already exist!Please login','success')
            return redirect(url_for('pregister'))
        if not(len(name)) >3:
            flash('length of name is invalid','error')
            return redirect(url_for('pregister')) 
        if (len(mobile))<10:
            flash('invalid mobile number','error')
            return redirect(url_for('pregister')) 
        if (len(password))<8:
            flash('length of password should be greater than 7','error')
            return redirect(url_for('pregister'))
        else:
             flash('You have registtered succesfully','success')
            
        entry = Pregister(name=name ,uname=uname,mobile=mobile,email=email,password=password,cpassword=cpassword)
        db.session.add(entry)
        db.session.commit()
    return render_template('pregister.html',params=params)

@app.route("/plogin.html",methods=['GET','POST'])
def plogin():
    if (request.method== "GET"):
        if('email' in session and session['email']):
            return render_template('parent_dashboard.html',params=params)
        else:
            return render_template("plogin.html", params=params)

    if (request.method== "POST"):
        email = request.form.get('email')
        password = request.form["password"]
        
        login = Pregister.query.filter_by(email=email, password=password).first()
        if login is not None:
            session['email']=email
            return render_template('parent_dashboard.html',params=params)
        else:
            flash("plz enter right password",'error')
            return render_template('plogin.html',params=params)



@app.route("/pcontact",methods=['GET','POST'])
def pcontact():
    if(request.method=='POST'):
        name=request.form.get('name')
        child_name=request.form.get('child_name')
        email=request.form.get('email')
        subject =request.form.get('subject')
        message=request.form.get('message')
        entry=Pcontact(name=name,child_name=child_name,email=email,subject=subject,message=message)
        db.session.add(entry)
        db.session.commit()
    return render_template('/pcontact.html',params=params)

@app.route("/contact.html",  methods=['GET','POST'])
def contact():
    if(request.method =='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        subject=request.form.get('subject')
        message=request.form.get('message')
        entry=Contact(name=name,email=email,subject=subject,message=message)
        db.session.add(entry)
        db.session.commit()
    return render_template('/contact.html',params=params)

@app.route("/attendence")
def Attendance():

    return render_template("attendence.html")

@app.route("/student_dashboard.html")
def sdashboard():
    return render_template("student_dashboard.html", params=params)

@app.route("/parent_dashboard.html")
def pdashboard():
    if('email' in session and session['email']):
        email=session['email']
        info=Pregister.query.filter_by( email=session['email'])
        print(info)
        return render_template("parent_dashboard.html", params=params,email=email,info=info)

@app.route("/generate.html", methods=['GET','POST'])
def Generate():
    # f = open('students.txt','r')
    # lines = f.read().split("\n")
    # print(lines)
    email=session['email']
    conn = sql_db.connect(user='root',host='localhost',password ='',database='attendence')
    mycursor = conn.cursor()
    sql = 'SELECT subject FROM register WHERE email= %s'
    tuple=(email,)
    mycursor.execute(sql,tuple)
    sub_result = mycursor.fetchall()
    conn.close()
    teacher_sub=(sub_result[0][0])
    sub_list=decode_binary(teacher_sub)

    if request.method=='POST':

        year=request.form.get('year')
        branch=request.form.get('branch')
        subject=request.form.get('subject')
        conn = sql_db.connect(user='root',host='localhost',password ='',database='attendence')
        mycursor = conn.cursor()
        sql = 'SELECT Sid, email,name FROM sregister WHERE year= %s AND branch= %s'
        tuple=(year,branch)
        mycursor.execute(sql,tuple)
        result = mycursor.fetchall()
        conn.close()
        
        ts=time.time()
        append_ts=int(ts)
        
        email_file=[]
        myobj = datetime.now()
        lecture_time=str(myobj.time())
        lecture_date = str(myobj.date()) 

        for Sid in range (0,len(result)):
            data = result[Sid][0]
            email=result[Sid][1]
            name=result[Sid][2]
            file_name=str(result[Sid][0]+'.png')
            email_file.append({'email':email,'file':file_name})
            entry = Attend(Sid=data,Semail=email,Sname=name,Temail=session['email'],branch=branch,Subject=subject,Year=year,Status='A',Time=lecture_time,Date=lecture_date,QRtime=str(append_ts))
            db.session.add(entry)
            db.session.commit()
            #print(type(email))
            version,level,qr = myqr.run(
                str(data + " " + str(append_ts)),
                level='H',
                version=1,
                colorized=True,
                contrast=1.0,
                brightness=1.0,
                save_name = str(result[Sid][0]+'.png'),
                save_dir=os.getcwd()
                )
        Promise.all([send_mail(i) for i in email_file])
            
    return render_template('generate.html',sub_list=sub_list)

@app.route("/scanqr.html")
def Scan():
    return render_template('scanqr.html')


@app.route('/student_dashboard')
def update():
    
    import db1
    return render_template('student_dashboard.html')



@app.route('/line_chart')
def line():
    
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Attendence System', max=30 , labels=line_labels, values=line_values)
   

@app.route("/view.html" ,methods=['GET','POST'])
def View():
    email=session['email']
    conn = sql_db.connect(user='root',host='localhost',password ='',database='attendence')
    mycursor = conn.cursor()
    sql = 'SELECT subject FROM register WHERE email= %s'
    tuple=(email,)
    mycursor.execute(sql,tuple)
    sub_result = mycursor.fetchall()
    conn.close()
    teacher_sub=(sub_result[0][0])
    sub_list=decode_binary(teacher_sub)
    result=[]
    if request.method=='POST':

        year=request.form.get('year')
        branch=request.form.get('branch')
        subject=request.form.get('subject')
        from_date = str(request.form.get('from-date'))
        to_date = str(request.form.get('to-date'))
        print(from_date)
        conn = sql_db.connect(user='root',host='localhost',password ='',database='attendence')
        mycursor = conn.cursor()
        #myobj = datetime.now()
        #lecture_date = str(myobj.date())
        sql = 'SELECT * FROM attend WHERE year= %s AND branch= %s AND Subject= %s AND Date BETWEEN %s AND %s'
        tuple=(year,branch,subject,from_date,to_date)
        mycursor.execute(sql,tuple)
        result = mycursor.fetchall()
        sql_status = 'SELECT COUNT(*) FROM attend WHERE Status = %s AND year= %s AND branch= %s AND Subject= %s AND Date BETWEEN %s AND %s'
        tuple_status=('P',year,branch,subject,from_date,to_date)
        mycursor.execute(sql_status,tuple_status)
        result_status = mycursor.fetchall()
        conn.close()

        print(result_status[0][0])
        sid_list=[]
        res_list=[]
        for i in result:
            if i[1] not in sid_list:
                sid_list.append(i[1])
                if i[8]=='P':

                    obj={'sid':i[1],'name':i[2],'attend':1,'total':1}
                else:
                    obj={'sid':i[1],'name':i[2],'attend':0,'total':1}
                res_list.append(obj)
            else:
                for j in res_list:
                    if j['sid']==i[1]:
                        if i[8]=='P':
                            j['attend'] = j['attend'] + 1
                            j['total'] = j['total'] + 1
                        else:
                            j['total'] = j['total'] + 1

        
        print(res_list)

                    

        
        return render_template('view.html', params=params, regi=result,sub_list=sub_list ,total_attend = res_list,total_present = result_status[0][0])


    return render_template('view.html', params=params, regi=result,sub_list=sub_list)



@app.route("/studentq")
def Student_q():
    contacts = Contact.query.all()
    print(contacts)
    return render_template('studentq.html', params=params, con=contacts)

@app.route("/parentq")
def Parent_q():
    pcontacts = Pcontact.query.all()
    print(pcontacts)
    return render_template('parentq.html', params=params, pcon=pcontacts)

def Display():
    conn =  sql_db.connect(user='root',host='localhost',password ='',database='attendence')
    mycursor = conn.cursor()
    sql = '''SELECT COUNT(*) Period FROM attend where Sid="b'Co5617'"'''
    mycursor.execute(sql)
    myresult = mycursor.fetchone()[0]
    conn.close()
    return myresult

def Count():
    conn = sql_db.connect(user='root',host='localhost',password ='',database='attendence')
    mycursor = conn.cursor()
    sql = 'SELECT Sid,COUNT(Sid) FROM attend GROUP BY  Sid ORDER BY COUNT(Sid) DESC' ;
    mycursor.execute(sql)
    result = mycursor.fetchall()
    conn.close()
    return result

@app.route('/display')
def index():
    myresult = Display()
    result = Count()
    return render_template('display.html',myresult=myresult,result=result)
   
    

@app.route('/display.html')
def View1():
    import db1
    return render_template('display.html')
    

@app.route("/logout", methods = ['GET','POST'])
def logout():
    session.pop('email')
    return redirect(url_for('Home'))

@app.route('/result',methods=['GET','POST'])
def Mail():
    import g
    return render_template('/result.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)