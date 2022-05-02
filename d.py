from flask import Flask, Markup, render_template
import mysql.connector
import numpy as np
app = Flask(__name__,template_folder='templates')



mydb = mysql.connector.connect(host="localhost",
							user="root",
							password='',
							database="attendence")
mycursor = mydb.cursor()

# Fecthing Data From mysql to my python progame
mycursor.execute('''select Period,Date from attend ''')
result = mycursor.fetchall

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



@app.route('/line_chart')
def line():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Attendence System', max=100 , labels=line_labels, values=line_values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)