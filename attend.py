from tkinter.constants import GROOVE, RAISED, RIDGE
import cv2
import pyzbar.pyzbar as pyzbar
import time
import datetime
import csv
import mysql.connector

from datetime import date, datetime
import tkinter as tk 
from tkinter import Frame, ttk, messagebox
from tkinter import *

window = tk.Tk()
window.title('Attendance System')
window.geometry('1000x1000') 
                          
                          
year= tk.StringVar()      
branch= tk.StringVar()
sec= tk.StringVar() 
period= tk.StringVar()



title = tk.Label(window,text="Attendance System",bd=10,relief=tk.GROOVE,font=("times new roman",40),bg="lavender",fg="black")
title.pack(side=tk.TOP,fill=tk.X)

Manage_Frame=Frame(window,bg="lavender")
Manage_Frame.place(x=0,y=80,width=480,height=530)

ttk.Label(window, text = "Year",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=150)
combo_search=ttk.Combobox(window,textvariable=year,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('1','2','3','4') 
combo_search.place(x=250,y=150)

ttk.Label(window, text = "Branch",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=200)
combo_search=ttk.Combobox(window,textvariable=branch,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=("IT","COMP")
combo_search.place(x=250,y=200)

ttk.Label(window, text = "Section",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=250)
combo_search=ttk.Combobox(window,textvariable=sec,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('A','B','C','D')
combo_search.place(x=250,y=250)

ttk.Label(window, text = "Period",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=300)
combo_search=ttk.Combobox(window,textvariable=period,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('C','C++','Python','Java','m1','m2')
combo_search.place(x=250,y=300)







def checkk():
    if(year.get() and branch.get() and period.get() and sec.get()):
        window.destroy()
    else:
        messagebox.showwarning("Warning", "All fields required!!")
exit_button = tk.Button(window,width=13, text="Submit",font=("Times New Roman", 15),command=checkk,bd=2,relief=RIDGE)
exit_button.place(x=300,y=380)

Manag_Frame=Frame(window,bg="lavender")
Manag_Frame.place(x=480,y=80,width=450,height=530)
canvas = Canvas(Manag_Frame, width = 300, height = 300,background="lavender")      
canvas.pack()      
img = PhotoImage(file="Bg.png")      
canvas.create_image(50,50, anchor=NW, image=img) 

window.mainloop()

cap = cv2.VideoCapture(0)
Sid=[]
today=date.today()
d= today

fob=open('d.csv','w+')
fob.write("Sid"+',')
fob.write("branch"+',')
fob.write("Sec"+',')
fob.write("Year"+',')
fob.write("Period"+',')
fob.write("Time"+',')
fob.write("Date"+'\n')




def enterData(z):
    if z in Sid:
        pass
    else:
        it=datetime.now()
        Sid.append(z)
        z=''.join(str(z))
        time = it.strftime("%I:%M:%S")
        date = it.strftime("%p %x")
        
        
        fob.write(z+','+branch.get()+','+sec.get()+','+year.get()+','+period.get()+','+time+','+date+'\n')
        
    return Sid 
    
print('Reading...')







def checkData(data):
    
    if data in Sid:
        print('Already Present')
    else:
        print('\n'+str(len(Sid)+1)+'\n'+'present...')
        enterData(data)
        
       

while True:
    _, frame = cap.read()         
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)
       
    cv2.imshow("Frame", frame)
    

    if cv2.waitKey(1)&0xFF == ord('g'):
        cv2.destroyAllWindows()
        break





