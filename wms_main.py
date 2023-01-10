#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sooryankc, faez
"""
print('''    _____________________________________________________     
    888       888   .d8888b.    888b     d888   .d8888b.     
    888   o   888  d88P   Y88b  8888b   d8888  d88P  Y88b    
    888  d8b  888  888     888  88888b.d88888  Y88b.         
    888 d888b 888  888          888Y88888P888   "Y888b.      
    888d88888b888  888          888 Y888P 888      "Y88b.    
    88888P Y88888  888     888  888  Y8P  888        "888    
    8888P   Y8888  Y88b   d88P  888   "   888  Y88b  d88P    
    888P     Y888    "Y8888P"   888       888   "Y8888P"     
    _____________________________________________________ ''')   
print()

print('Welcome!!\nYou have now entered the waste collection management portal')
import mysql.connector
import tabulate
m_con=mysql.connector.connect(host='localhost',user='root',password='french')
m_cur=m_con.cursor()
m_cur.execute('CREATE DATABASE IF NOT EXISTS WMS')
m_cur.execute('USE WMS')
m_cur.execute('''CREATE TABLE IF NOT EXISTS sector_w(sec_id int not null,
                                                    worker_id varchar(5) primary key not null,
                                                    worker_name varchar(255) not null,
                                                    w_address varchar(255) not null,
                                                    w_phno varchar(255) )''')
m_cur.execute('''CREATE TABLE IF NOT EXISTS sector_h(house_id int primary key not null,
                                                    address varchar(255) unique not null,
                                                    resident_name varchar(255) not null,
                                                    resident_phno varchar(255) ,
                                                    sec_id int not null)''')
m_cur.execute('''CREATE TABLE IF NOT EXISTS record(date varchar(12) not null,
                                                    house_id int primary key not null,
                                                    w_coll_status varchar(255) default 'not collected',
                                                    pay_amount int not null default 0,
                                                    pay_status varchar(255) default 'unpaid')''')
m_con.commit()
m_con.close()
def ed_w():
    m_con=mysql.connector.connect(host='localhost',user='root',password='french')
    m_cur=m_con.cursor()
    m_cur.execute('USE WMS')
    while True:
        print('\nPress 1 to Add a new worker\npress 2 to edit the existing details\nPress 3 to delete a data\nPress 4 to Exit')
        c_s=int(input('Enter your Choice: '))
        if c_s==1:
            w1=int(input('Enter the Sector Number: '))
            w2=input('Enter the Worker ID: ')
            w3=input('Enter the name of the worker: ')
            w4=input('Enter The Residence Address: ')
            w5=int(input('Enter the Contact No: '))
            m_cur.execute('USE WMS')
            m_cur.execute('INSERT INTO sector_w VALUES({},"{}","{}","{}","{}")'.format(w1,w2,w3,w4,w5))
            m_con.commit()
            print('Values inserted successfully')
        elif c_s==2:
            m_cur.execute('USE WMS')
            print('\nPress 1 to change the Residence Address\nPress 2 to change the contact information')
            c_s2=int(input('Enter your Choice: '))
            if c_s2==1:
                sid=input('Enter the Worker ID: ')
                a=input('Enter the New Address: ')
                cm='UPDATE sector_w SET w_address="{}" WHERE worker_id="{}"'.format(a,sid)
                m_cur.execute(cm)
                m_con.commit()
                print('Changes inserted successfully')
            elif c_s2==2:
                sid=input('Enter the Worker ID: ')
                con=input('Enter the Phone Number: ')
                cm='UPDATE sector_w SET w_phno="{}" WHERE worker_id="{}"'.format(con,sid)
                m_cur.execute(cm)
                m_con.commit()
                print('Changes inserted successfully')
        elif c_s==3:
            sid=input('Enter the Worker ID:')
            cm='DELETE FROM sector_w WHERE worker_id="{}"'.format(sid)
            m_cur.execute(cm)
            m_con.commit()  
            print('Deleted successfully')
        elif c_s==4:
            print('exit')
            break
        else:
            print('Please enter a valid option')
def ed_h():
    m_con=mysql.connector.connect(host='localhost',user='root',password='french')
    m_cur=m_con.cursor()
    m_cur.execute('USE WMS')
    while True:
        print('\nPress 1 to Add a New House\nPress 2 to Edit the Details\nPress 3 to Delete a Data\nPress 0 to Exit')
        c_h=int(input('Enter your choice: '))
        m_cur.execute('USE WMS')
        if c_h==1:
            h1=int(input('Enter your House ID: '))
            h2=input('Enter the House Address: ')
            h3=input('Enter the name of the resident: ')
            h4=int(input('Enter the Sector Number: '))
            h5=int(input('Enter the Contact Number of the Resident: '))
            m_cur.execute('INSERT INTO sector_h VALUES({},"{}","{}","{}",{})'.format(h1,h2,h3,h5,h4))
            m_con.commit()
            print('Values inserted successfully')
        elif c_h==3:
            hid=int(input('Enter the House ID: '))
            cm='DELETE FROM sector_h WHERE house_id={}'.format(hid)
            m_cur.execute(cm)
            m_con.commit()
            print('Deleted successfully')
        elif c_h==4:
            print('Exit')
            break    
        elif c_h==2:
            c_h2=None
            while c_h2!=0:
                print('Press 1 to Change the Residence Address\nPress 2 to change the Contact No.\nPress 3 to Change the Resident Name\nPress 0 to Exit')
                c_h2=int(input('Enter your Choice: '))
            hid=int(input('Enter your House ID: '))
            if c_h2==1:
                a=input('Enter address: ')
                cm='UPDATE sector_h SET address={} WHERE house_id={}'.format(a,hid)
                m_cur.execute(cm)
                m_con.commit()
                print('Changes inserted successfully')
            elif c_h2==2:
                n=input("Enter the Resident's Phone No.: ")
                cm='UPDATE sector_h SET resident_phno="{}" WHERE house_id={}'.format(n,hid)
                m_cur.execute(cm)
                m_con.commit()
                print('Changes inserted successfully')
            elif c_h2==3:
                n=input('Enter the New Resident Name:')
                cm='UPDATE sector_h SET resident_name="{}" WHERE house_id{}'
                m_cur.execute(cm)
                m_con.commit()
                print('Changes inserted successfully')
            elif c_h2==0:
                print('Changes not inserted')
                break
            else:
                print('Please enter a valid option')
        elif c_h==0:
            print('Changes not inserted')
            break
        else:
            print('Please enter a valid option')
        
def ed_r():
    m_con=mysql.connector.connect(host='localhost',user='root',password='french')
    m_cur=m_con.cursor()
    m_cur.execute('USE WMS')
    while True:
        print('\nPress 1 to Enter a New Data\nPress 2 to Update your Payment Status\nPress 3 to Update your Waste Collection Status\nPress 4 to Exit')
        c_r=int(input('Enter your Choice: '))
        if c_r==1:
            r0=input('Enter the date(dd/mm/yyyy): ')
            r1=int(input('Enter your House ID: '))
            r2=input('Enter the Waste Collection Status(Collected/Not Collected): ')
            if r2=='Not Collected'.lower():
                m_cur.execute('INSERT INTO record(date,house_id,w_coll_status,pay_status) VALUES("{}",{},"{}","{}")'.format(r0,r1,r2,r4))                
            else:
                r3=int(input('Enter the Amount to be Paid: '))
            r4=input('Enter your Payment Staus(Paid/Unpaid): ')
            m_cur.execute('INSERT INTO record VALUES("{}",{},"{}",{},"{}")'.format(r0,r1,r2,r3,r4))
            m_con.commit()
            print('Values inserted successfully')
        elif c_r==2:
            hid=int(input('Enter your House ID: '))
            st=input('Enter your Payment Staus(Paid/Unpaid): ')
            cm='UPDATE record SET pay_status={} WHERE house_id={}'.format(st,hid)
            m_cur.execute(cm)
            m_con.commit()
            print('Changes inserted successfully')
        elif c_r==3:
            hid=int(input('Enter your House ID: '))
            st=input('Enter the Waste Collection Status(Collected/Not Collected): ')
            cm='UPDATE record SET w_coll_status={} WHERE house_id={}'.format(st,hid)
            m_cur.execute(cm)
            m_con.commit()
            print('Changes inserted successfully')
        elif c_r==4:
            print('Exit')
            break
        else:
            print('Please enter a valid option')

def sh_w():
    m_con=mysql.connector.connect(host='localhost',user='root',password='french')
    m_cur=m_con.cursor()
    valueList=[]
    m_cur.execute('USE WMS')
    m_cur.execute('SELECT * FROM sector_w')
    row=m_cur.fetchall()
    for r in row:
        valueList.append(r)
    headers=['Sector','Worker ID','Worker Name','Worker Adress','Phone No.']
    print(tabulate.tabulate(valueList,headers,tablefmt="rounded_grid"))
    
def sh_h():
    m_con=mysql.connector.connect(host='localhost',user='root',password='french')
    m_cur=m_con.cursor()
    valueList=[]
    m_cur.execute('USE WMS')
    m_cur.execute('SELECT * FROM sector_h')
    row=m_cur.fetchall()
    headers=['House ID','Address','Resident Name','Phone No.','Sector']
    for r in row:
        valueList.append(r)
    print(tabulate.tabulate(valueList,headers,tablefmt="rounded_grid"))
def sh_r():
    m_con=mysql.connector.connect(host='localhost',user='root',password='french')
    m_cur=m_con.cursor()
    valueList=[]
    m_cur.execute('USE WMS')
    m_cur.execute('SELECT * FROM record')
    row=m_cur.fetchall()
    headers=['Date','House ID','Waste Collection status','Payment Amount','Payment Status']
    for r in row:
        valueList.append(r)
    print(tabulate.tabulate(valueList,headers,tablefmt="rounded_grid"))

while True:
    print('\nPress 1 to Access The Workers List\nPress 2 to Access The House List\nPress 3 to Access The Records\nPress 4 to Exit')
    c=int(input('Enter your choice: '))
    if c==1:
        print('\nYou have now entered the Workers List')
        print('Press 1 to Edit The List\nPress 2 to View The List')
        c2=int(input('Enter your Choice: '))
        if c2==1:
            ed_w()
        elif c2==2:
            sh_w()
    elif c==2:
        print('\nYou have now entered the House List')
        print("Press 1 to Edit The List\nPress 2 to View The List")
        c2=int(input('Enter your Choice: '))
        if c2==1:
            ed_h()
        elif c2==2:
            sh_h()
    elif c==3:
        print('\nYou have now entered the Records')
        print("Press 1 to Edit The List\nPress 2 to View The List")
        c2=int(input('Enter your Choice: '))
        if c2==1:
            ed_r()
        elif c2==2:
            sh_r()
    elif c==4:
        print('Thank you for using our services!!')
        print('Bye')
        break
    else:
        print('Please enter a valid option')
