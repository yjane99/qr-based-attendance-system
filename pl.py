import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser


conn = sqlite3.connect('student_Attendence.db')
cursor = conn.cursor()
print("Opened database successfully")


def graph_data():
    conn.execute('''SELECT Period,Date  FROM attend where Sid="b'Co5615'"''')
    data = cursor.fetchall()

    Period = []
    Date = []
    
    for row in data:
        Period.append((row[0]))
        Date.append(row[1])

    plt.plot_date(Period,Date,'-')
    plt.show()
graph_data()