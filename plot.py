from flask import Flask, render_template, request,session,redirect,flash,url_for
import io
import base64
import mysql.connector
import matplotlib.pyplot as plt



app = Flask(__name__,template_folder='templates')
@app.route('/plot')
def Plotting():
    img = io.BytesIO()
    mydb = mysql.connector.connect(host='localhost',user='root',password='',database='attendence')
    print("database connected!")
    cursor=mydb.cursor()
    cursor.execute('''SELECT Period , Time FROM attend where Sid = "b'Co5618'"''')
    data = cursor.fetchall()
    Period = []
    Time = []
    
    for row in data:
        Period.append(row[0])
        Time.append(row[1])
        
        plt.plot(Period,Time,'-')
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        return render_template('<img src="data:image/png;base64,{}">'.format(plot_url))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)