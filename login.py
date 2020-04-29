from tkinter import *
import os
import tkinter.messagebox as MessageBox
import pymysql
import pandas as pd


data=pd.read_csv(r'C:\\Users\\User\AppData\\Local\\Programs\\Python\\Python38-32\\Itvedant_project\\login.csv')

def validation():
    
    uid=username_login_entry.get()
    p=password__login_entry.get()
    if(uid=="" and p==""):
        MessageBox.showinfo("Fetch Employee","ID and password are compulsory for fetch")
    
    elif uid not in data['userid'].values and p not in data['password'].values:
        MessageBox.showinfo("login error","Incorrect ID and password !!!")
        username_login_entry.delete(0,END)
        password__login_entry.delete(0,END)
    
    else:
        conn = pymysql.connect(host='localhost',user='root',
                                password='',database='bank_database'
                                )

        cursor = conn.cursor()
        q= "SELECT * from login where userid='" + uid + "' and password='" + p + "'"
        #Execute cursor and pass query of Emloyee and data of Emloyee
        cursor.execute(q)
        rows=cursor.fetchall()
        for row in rows:
            os.system('python Banking_managment_system.py')
        conn.close()
        username_login_entry.delete(0,END)
        password__login_entry.delete(0,END)

        
login_screen=Tk()
login_screen.title("Login")
login_screen.configure(bg='lemon chiffon')
login_screen.geometry("300x250")
Label(login_screen, text="Login : ",fg='black',bg='lemon chiffon',font=("Sylfaen", 15),pady=2).grid(row=0,column=1,columnspan=2)
Label(login_screen, text="Username :",font="Times 10 bold",bg='lemon chiffon').grid(row=1,column=0)
username_login_entry = Entry(login_screen,justify=RIGHT,width=20,bg='PaleTurquoise1')
username_login_entry.grid(row=1,column=1,padx=10,pady=10)
Label(login_screen, text="Password : ",font="Times 10 bold",bg='lemon chiffon').grid(row=2,column=0)
password__login_entry = Entry(login_screen, show= '*',justify=RIGHT,width=20,bg='PaleTurquoise1')
password__login_entry.grid(row=2,column=1,padx=10,pady=10)
Button(login_screen, text="Login", width=20,height=1,command=validation,bg='spring green',borderwidth=3,font="Times 10 bold",relief=RAISED).grid(row=3,column=1,columnspan=2)
login_screen.mainloop()

