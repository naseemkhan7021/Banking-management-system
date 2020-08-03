from tkinter import *
from tkinter import ttk,messagebox 
from datetime import date
import random
import pymysql
import pandas as pd
from csv import DictWriter
# import import pdb



def append_dict_as_row(file_name, dict_of_elem, field_names):       #to creat the .csv file
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)


def createDatabase():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password=''
    )

    if conn:
        try:
            cors = conn.cursor()
            value = cors.execute("CREATE DATABASE IF NOT EXISTS banck_database;")
            if value == False:
                print("Data server is Thare !! \n Please check Database servar The database exit or any problame")

            else:
                if value == True:
                    try:
                        conn = pymysql.connect(
                            host='localhost',
                            user='root',
                            password='',
                            database='banck_database'
                        )
                        query = """CREATE TABLE IF NOT EXISTS customers (CustName VARCHAR(255), CustID INT(10),AcOpeningDate DATE,JointHolderName VARCHAR(20),Address VARCHAR(50),City VARCHAR(50),PinCode VARCHAR(50),State VARCHAR(50),Country VARCHAR(50),ResTelNo VARCHAR(50),MobilNo VARCHAR(50),Occupation VARCHAR(50),AcType VARCHAR(50),AcNo INT(20)
                        )"""
                        cors = conn.cursor()
                        cors.execute(query)
                        conn.commit()
                        print('successfully ...')
                    
                    except Exception as b:
                        conn = pymysql.connect(
                            host='localhost',
                            user='root',
                            password=''
                        )
                        cors = conn.cursor()
                        value = cors.execute("DROP DATABASE banck_database;")
                        # value = cors.execute("DROP DATABASE datak_com;")
                        conn.commit()
                        print(f'erro is {b}')
                        # messagebox.showinfo("Alert","Your database is deleted becouse table is not currect !!! \n(please check database.)")
                        messagebox.showwarning("Alert","Your database is deleted becouse table is not currect !!! \n(please check database.)")
        except Exception:
            pass



createDatabase()

def submit1():
    try:
        #connect to the database

        connection = pymysql.connect(host='localhost',user='root',
                                        password='',database='banck_database'
                                    )

        #connect() inbuilt function of pymysql library
        #connection user defined object

        print('connection successful!!')
    except Exception:
        messagebox.showinfo("Error","Data server Error !!! \n (Please check Database servar)")

    #cursor user defined object
    cursor = connection.cursor() # cursor inbuilt method of pymysql.connect() ,to active(open) the connection
    #q user defined
    q= """INSERT INTO customers (CustName,CustID,AcOpeningDate,JointHolderName,Address,City,PinCode,State,Country,
                                    ResTelNo,MobilNo,Occupation,AcType,AcNo)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    try:
        if len(mobile_E.get())==10 and len(TelNo_E.get())==10:
            #Esecute cursor and pass query of student and data of student
            #user defind input
            cname=cutname_E.get()
            cid=random.randint(100000,999999)
            acod=Acdate_E.get()
            Jhln=Nomini_E.get()
            Ad=Adderess_E.get()
            ci=City_E.get()
            PC=Pincod_E.get()
            St=State_E.get()
            Cn=Country_E.get()
            RTno=TelNo_E.get()
            Mno=mobile_E.get()
            Oction=Occupt.get()
            AcTp=AcT.get()
            Acno=random.randint(100000000000000,999999999999999)
            

            val=(cname,cid,acod,Jhln,Ad,ci,PC,St,Cn,RTno,Mno,Oction,AcTp,Acno)
            cursor.execute(q,val) #run sql query and data send from puthon to mysql here execute() inbuilt method of cursor
            connection.commit() #to save action in table through query

            field_names=['CustName','CustID','AcOpeningDate','JointHolderName','Address','City','PinCode','State','Country','ResTelNo','MobilNo'
                        ,'Occupation','AcType','AcNo'
                        ]

            # dict for store the data
            dic={   'CustName'      :cname,  'CustID'           :cid,
                    'AcOpeningDate' :acod,   'JointHolderName'  :Jhln,
                    'Address'       :Ad,     'City'             :ci,
                    'PinCode'       :PC,     'State'            :St,
                    'Country'       :Cn,     'ResTelNo'         :RTno,
                    'MobilNo'       :Mno,    'Occupation'       :Oction,
                    'AcType'        :AcTp,    'AcNo'            :Acno
                    
                }
             
            
            append_dict_as_row(r'C:\\Users\\User\AppData\\Local\\Programs\\Python\\Python38-32\\Itvedant_project\\cutomer_info.csv',dic,field_names)      #to creat the .csv file

            print(cursor.rowcount, "Record Inserted")
            print('Your details is here \n Check your details and note it ')
            print(dic)  # print only one row data

            messagebox.showinfo("Alert","The Record is successfully inserted !!! \n (ThanYou for opening account)")

            cutname_E.delete(0, END)
            Acdate_E.delete(0, END)
            Nomini_E.delete(0, END)
            Adderess_E.delete(0, END)
            City_E.delete(0, END)
            Pincod_E.delete(0, END)
            State_E.delete(0, END)
            Country_E.delete(0, END)
            TelNo_E.delete(0, END)
            mobile_E.delete(0, END)
        else:
            messagebox.showinfo("Error","Mobile or Telphone No. is error !!! \n (Please Enter 10 digits No.)")
            mobile_E.delete(0, END)
            TelNo_E.delete(0, END)
    except Exception as e:
        print(f"sumthing is wrong{e}")

def showcutom_dedails():   # using pandas to read .csv file login fungtion
    data=pd.read_csv(r'C:\\Users\\User\AppData\\Local\\Programs\\Python\\Python38-32\\Itvedant_project\\login.csv')

    uid=username_login_entry.get()
    p=password__login_entry.get()
    if(uid=="" and p==""):
        messagebox.showerror("Fetch Employee","ID and password are compulsory for fetch")
    
    elif uid not in data['userid'].values and p not in data['password'].values:
        messagebox.showinfo("login error","Incorrect ID and password !!!")
        username_login_entry.delete(0,END)
        password__login_entry.delete(0,END)

    
    else:
        customfile=pd.read_csv(r'C:\\Users\\User\AppData\\Local\\Programs\\Python\\Python38-32\\Itvedant_project\\cutomer_info.csv')
        print(customfile)
        username_login_entry.delete(0,END)
        password__login_entry.delete(0,END)
        login_screen.destroy()

def searchrecord():
    #connect to the database

    connection = pymysql.connect(host='localhost',
                                    user='root',password='',
                                    database='banck_database'
                                )
    #connect() inbuilt function of pymysql library
    #connection user defined object
    print('connection successful!!')

    cursor = connection.cursor()      # to active(open) the connection


    q="select * from customers where AcNo=%s"
    cutmAC=cutAccountno_E.get()
    # Execute cursor
    cursor.execute(q,cutmAC)  #run SQL query aconn.commit() to save action in table through query 
    records=cursor.fetchall() # records user defined object which hold no. of rows and columns means hod table
    print('Total number of rows in customers is : ', cursor.rowcount)
    for row in records:
        print("Cutomer name         : ",row[0])
        print("Cutomer Id           : ",row[1])
        print("Accoutn opening date : ",row[2])
        print("Joint holder name    : ",row[3])
        print("Address              : ",row[4])
        print("City                 : ",row[5])
        print("Pincode              : ",row[6])
        print("State                : ",row[7])
        print("Country              : ",row[8])
        print("Teliphone no.        : ",row[9])
        print("Mobile no.           : ",row[10])
        print("Occupation           : ",row[11])
        print("Actype               : ",row[12])
        print("Ac No.               : ",row[13])
        break
    else:
        messagebox.showinfo("Error","Account no. does not exist !!! \n (Please Chack Account no. and retry)")


def customTransection():
    data=pd.read_csv(r'C:\\Users\\User\AppData\\Local\\Programs\\Python\\Python38-32\\Itvedant_project\\cutomer_info.csv')

    try:

        #connect to the database

        connection = pymysql.connect(host='localhost',user='root'
                                        ,password='',
                                        database='banck_database'
                                    )

        #connect() inbuilt function of pymysql library
        #connection user defined object

        print('connection successful!!')
    except Exception:
        messagebox.showinfo("Error","Data server Error !!! \n (Please check Database servar)")

    # #cursor user defined object
    cursor = connection.cursor() # cursor inbuilt method of pymysql.connect() ,to active(open) the connection
    # q user defined
        
    q= """INSERT INTO customerstransaction (CustomerAcNo,Date,Particulars,AmtWithdrown,AmtDeposited,Balance)
                                    VALUES (%s,%s,%s,%s,%s,%s)"""

    

    if int(cutAccountno_E.get()) in data['AcNo'].values and cutname_E.get() in data['CustName'].values:
        CaNo=cutAccountno_E.get()
        dt=date.today()
        prt=particular_E.get()
        amtW=Withmoney_E.get()
        amtD=Deposit_E.get()
        amtB=Deposit_E.get()

        val=(CaNo,dt,prt,amtW,amtD,amtB)
        cursor.execute(q,val)
        connection.commit()

        field_names=['CustomerAcNo','Date','Particulars',
                        'AmtWithdrow','AmtDeposited','Balance',
                    ]

        # dict for store the data
        dic1={'CustomerAcNo':    CaNo,
                'Date':         dt,
                'Particulars':  prt,
                'AmtWithdrow':  amtW,
                'AmtDeposited': amtD,
                'Balance':      amtB
                }
             
            
        append_dict_as_row(r'C:\\Users\\User\AppData\\Local\\Programs\\Python\\Python38-32\\Itvedant_project\\cutomerTrancection_info.csv'
                                ,dic1,field_names)      #to creat the .csv file

        print(cursor.rowcount, "Record Inserted")
        print('Your details is here \n Check your details and note it ')
        print(dic1)  # print only one row data

        messagebox.showinfo("Alert","The Record is successfully inserted !!! \n (ThanYou for Transection )")

        cutname_E.delete(0,END)
        cutAccountno_E.delete(0, END)
        particular_E.delete(0, END)
        Withmoney_E.delete(0, END)
        Deposit_E.delete(0,END)

    else:
        messagebox.showinfo("Error","Account no. or User name does not exist !!! \n (Please Check Account no. and retry)")
        cutAccountno_E.delete(0, END)


d = {1:"new Account",2:'Account info',3:'withdro money',4:'Deposit monye',5:'Cutomers list'}
print("pleas type number for folowing comment")


yn='y'
while yn=='y':
    for k,v in d.items():
        print(f"{k} for {v}")
    try:
        op=int(input("enter your option -->"))




        if op==1:
            wd=Tk()
            wd.title('New Account')
            wd.configure(bg='lemon chiffon')
            # flat, groove, raised, ridge, solid, or sunken   <-- this is border style

            HTitle=Label(wd,text='Enter Customer Dedails',bg='lemon chiffon',font=("Arial",20))
            HTitle.config(font=("Sylfaen", 30))
            HTitle.grid(row=0,column=1,columnspan=4)
            
            # labels 
            cutname_L=Label(wd,text="Customer name :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            cutname_L.grid(row=1,column=0)
            Acodate_L=Label(wd,text="Account oppening date :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Acodate_L.grid(row=1,column=2)
            Nomini_L=Label(wd,text="Joint holder name :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Nomini_L.grid(row=2,column=0)
            Adderess_L=Label(wd,text="Adderess :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Adderess_L.grid(row=2,column=2)
            City_L=Label(wd,text="city name :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            City_L.grid(row=3,column=0)
            PinCod_L=Label(wd,text="Pin code :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            PinCod_L.grid(row=3,column=2)
            State_L=Label(wd,text="State name :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            State_L.grid(row=4,column=0)
            Country_L=Label(wd,text="Country name :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Country_L.grid(row=4,column=2)
            TelNo_L=Label(wd,text="Telphone No. :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            TelNo_L.grid(row=5,column=0)
            MobileNo_L=Label(wd,text="Mobile No.` :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            MobileNo_L.grid(row=5,column=2)


            # Entry

            cutname_E=Entry(wd,justify=RIGHT,width=20,bg='PaleTurquoise1')
            cutname_E.grid(row=1,column=1,padx=10,pady=10)
            Acdate_E=Entry(wd,justify=RIGHT,width=20,bg='PaleTurquoise1')
            Acdate_E.grid(row=1,column=3,padx=10,pady=10)
            Nomini_E=Entry(wd,justify=RIGHT,width=20,bg='PaleTurquoise1')
            Nomini_E.grid(row=2,column=1,padx=10,pady=10)
            Adderess_E=Entry(wd,justify=RIGHT,width=20,bg='PaleTurquoise1')
            Adderess_E.grid(row=2,column=3,padx=10,pady=10)
            City_E=Entry(wd,justify=RIGHT,width=20,bg='PaleTurquoise1')
            City_E.grid(row=3,column=1,padx=10,pady=10)
            Pincod_E=Entry(wd,justify=RIGHT,width=20,bg='PaleTurquoise1')
            Pincod_E.grid(row=3,column=3,padx=10,pady=10)
            State_E=Entry(wd,justify=RIGHT,width=20,bg='PaleTurquoise1')
            State_E.grid(row=4,column=1,padx=10,pady=10)
            Country_E=Entry(wd,justify=RIGHT,width=20,bg='PaleTurquoise1')
            Country_E.grid(row=4,column=3,padx=10,pady=10)
            TelNo_E=Entry(wd,justify=RIGHT,width=20,bg='PaleTurquoise1')
            TelNo_E.grid(row=5,column=1,padx=10,pady=10)
            mobile_E=Entry(wd,justify=RIGHT,width=20,bg='PaleTurquoise1')
            mobile_E.grid(row=5,column=3,padx=10,pady=10)

            # combobuttons  accoute type

            Acctype=Label(wd,text="Account type :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Acctype.grid(row=6,column=0)
            # AcT=StringVar

            # combobox 1
            AcT=ttk.Combobox(wd)      # month user define object of combox(dropedowne menu)

            AcT["values"]=('Saving','Currant','Fixed')
            AcT.grid(row=6,column=1)
            AcT.current(1)



            # combobox 2
            Occupt_L=Label(wd,text="Choice your occupation :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Occupt_L.grid(row=6,column=2,padx=10,pady=10)

            Occupt=ttk.Combobox(wd)      # month user define object of combox(dropedowne menu)

            Occupt["values"]=('Student','Doctor','Businessman','House wifi','other')
            Occupt.grid(row=6,column=3)
            Occupt.current(1)

            #Button submit
            subBottun1=Button(wd,text="Submit",command=submit1,borderwidth=4,bg='spring green',fg='white', font="Times 12 bold",relief=RAISED,height=1,width=12)
            subBottun1.grid(row=8,column=1,columnspan=1)

            #Button close
            closB1=Button(wd,text="Close",command=wd.destroy,borderwidth=4,bg='red',fg='white', font="Times 12 bold",relief=RAISED,height=1,width=10)
            closB1.grid(row=8,column=2,columnspan=1)




            wd.mainloop()

        elif op==2:
            wd1=Tk()

            wd1.title('Account Info')
            wd1.configure(bg='lemon chiffon')

            HTitle2=Label(wd1,text='Account info',bg='lemon chiffon',font=("Arial",20))
            HTitle2.config(font=("Sylfaen", 30))
            HTitle2.grid(row=0,column=1,columnspan=4)

            # lable 
            cutname_L=Label(wd1,text="Customer name :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            cutname_L.grid(row=1,column=0)
            cutAccountno_L=Label(wd1,text="Customer Account no. : ",bg='lemon chiffon',font=("Arial"),padx=10,pady=10)
            cutAccountno_L.grid(row=1,column=3)

            # Entry
            nm=StringVar
            cutname_E=Entry(wd1,textvariable=nm,font=("Arial"),justify=RIGHT,width=20,bg='PaleTurquoise1')
            cutname_E.grid(row=1,column=2,padx=10,pady=10)
            cutAccountno_E=Entry(wd1,font=("Arial"),justify=RIGHT,width=20,bg='PaleTurquoise1')
            cutAccountno_E.grid(row=1,column=4,padx=10,pady=10)


            # submit Button
            subBottun2=Button(wd1,text="Submit",command=searchrecord,borderwidth=4,bg='spring green',font="Times 12 bold",relief=RAISED,height=1,width=12)
            subBottun2.grid(row=3,column=1)

            #Button close
            closB2=Button(wd1,text="Close",command=wd1.destroy,borderwidth=4,bg='red',font="Times 12 bold",relief=RAISED,height=1,width=10)
            closB2.grid(row=3,column=2)


            wd1.mainloop()

        elif op==3:
            wd2=Tk()
            wd2.title('Withdrow money')
            wd2.configure(bg='lemon chiffon')

            HTitle3=Label(wd2,text='Withdrow money',bg='lemon chiffon',font=("Arial",20))
            HTitle3.config(font=("Sylfaen", 30))
            HTitle3.grid(row=0,column=1,columnspan=4)


            # lable 
            cutname_L=Label(wd2,text="Customer name :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            cutname_L.grid(row=1,column=0)

            cutAccountno_L=Label(wd2,text="Customer Account no. : ",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            cutAccountno_L.grid(row=1,column=2)

            Withmoney_L=Label(wd2,text="Enter Withdrow money :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Withmoney_L.grid(row=2,column=0)

            Particular_L=Label(wd2,text="Particular :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Particular_L.grid(row=2,column=2)

            Deposit_L=Label(wd2,text="Enter Deposite money :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Deposit_L.grid(row=3,column=0)

            # Entry
            cutname_E=Entry(wd2,font=("Arial"),justify=RIGHT,width=20,bg='PaleTurquoise1')
            cutname_E.grid(row=1,column=1,padx=10,pady=10)

            cutAccountno_E=Entry(wd2,font=("Arial"),justify=RIGHT,width=20,bg='PaleTurquoise1')
            cutAccountno_E.grid(row=1,column=3,padx=10,pady=10)

            
            Withmoney_E=Entry(wd2,font=("Arial"),justify=RIGHT,width=20,bg='PaleTurquoise1')
            Withmoney_E.grid(row=2,column=1,padx=10,pady=10)

            particular_E=Entry(wd2,font=("Arial"),justify=RIGHT,width=20,bg='PaleTurquoise1')
            particular_E.grid(row=2,column=3,padx=10,pady=10)

            dc=StringVar()
            Deposit_E=Entry(wd2,font=("Arial"),textvariable=dc,justify=RIGHT,width=20,bg='PaleTurquoise1')
            Deposit_E.grid(row=3,column=1,padx=10,pady=10)
            
            dc.set('Please enter !! null')

            # submit Button
            subBottun3=Button(wd2,text="Submit",command=customTransection,borderwidth=4,bg='spring green',font="Times 12 bold",relief=RAISED,height=1,width=12)
            subBottun3.grid(row=4,column=1,columnspan=2)

            #Button close
            closB3=Button(wd2,text="Close",command=wd2.destroy,borderwidth=4,bg='red',font="Times 12 bold",relief=RAISED,height=1,width=10)
            closB3.grid(row=4,column=2,padx=2,columnspan=2)
            wd2.mainloop()


        elif op==4:
            wd3=Tk()

            wd3.title('Deposit money')
            wd3.configure(bg='lemon chiffon')

            HTitle4=Label(wd3,text='Deposit money',bg='lemon chiffon',font=("Arial",20))
            HTitle4.config(font=("Sylfaen", 30))
            HTitle4.grid(row=0,column=1,columnspan=4)


            # lable 
            cutname_L=Label(wd3,text="Customer name :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            cutname_L.grid(row=1,column=0)
            
            cutAccountno_L=Label(wd3,text="Customer Account no. : ",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            cutAccountno_L.grid(row=1,column=2)

            Deposit_L=Label(wd3,text="Enter Deposite money :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Deposit_L.grid(row=2,column=0)

            Particular_L=Label(wd3,text="Particular :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Particular_L.grid(row=2,column=2)

            Withmoney_L=Label(wd3,text="Enter Withdrow money :",font=("Arial"),bg='lemon chiffon',padx=10,pady=10)
            Withmoney_L.grid(row=3,column=0)

            # Entry

            cutname_E=Entry(wd3,font=("Arial"),justify=RIGHT,width=20,bg='PaleTurquoise1')
            cutname_E.grid(row=1,column=1,padx=10,pady=10)

            cutAccountno_E=Entry(wd3,font=("Arial"),justify=RIGHT,width=20,bg='PaleTurquoise1')
            cutAccountno_E.grid(row=1,column=3,padx=10,pady=10)

            particular_E=Entry(wd3,font=("Arial"),justify=RIGHT,width=20,bg='PaleTurquoise1')
            particular_E.grid(row=2,column=3,padx=10,pady=10)
            
            Deposit_E=Entry(wd3,font=("Arial"),justify=RIGHT,width=20,bg='PaleTurquoise1')
            Deposit_E.grid(row=2,column=1,padx=10,pady=10)

            wc=StringVar()
            Withmoney_E=Entry(wd3,font=("Arial"),textvariable=wc,justify=RIGHT,width=20,bg='PaleTurquoise1')
            Withmoney_E.grid(row=3,column=1,padx=10,pady=10)

            wc.set('Pleas enter !! null')

            # submit Button
            subBottun4=Button(wd3,text="Submit",command=customTransection,borderwidth=4,bg='spring green',font="Times 12 bold",relief=RAISED,height=1,width=12)
            subBottun4.grid(row=4,column=1,columnspan=2)

            #Button close
            closB3=Button(wd3,text="Close",command=wd3.destroy,borderwidth=4,bg='red',font="Times 12 bold",relief=RAISED,height=1,width=10)
            closB3.grid(row=4,column=2,padx=2,columnspan=2)

            wd3.mainloop()


        elif op==5:
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
            Button(login_screen, text="Login", width=20,height=1,command=showcutom_dedails,bg='spring green',borderwidth=3,font="Times 10 bold",relief=RAISED).grid(row=3,column=1,columnspan=2)
        
            #Button close
            Button(login_screen,text="Close",command=login_screen.destroy,borderwidth=3,bg='red',font="Times 10 bold",relief=RAISED).grid(row=4,column=1,padx=5,pady=2,columnspan=2)

            login_screen.mainloop()
            

        else:
            messagebox.showinfo('Error','please select only given no.')
            
        
    
    except ValueError:
        messagebox.showinfo('Error','Pleas write only number !!!!!')


    yn=input('Do you want to continue y/n ')
    
else:
    

    messagebox.showinfo('Thanck','Ok, Thanck for using program    !!!!!')
