#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 21:24:38 2022

@author: sooryankc
"""
print('--  __________________________________________________ --')
print('--  888_______888__.d8888b.__888b_____d888__.d8888b.__ --')
print('--  888___o___888_d88P__Y88b_8888b___d8888_d88P__Y88b_ --')
print('--  888__d8b__888_888____888_88888b.d88888_Y88b.______ --')
print('--  888_d888b_888_888________888Y88888P888__"Y888b.___ --')
print('--  888d88888b888_888________888_Y888P_888_____"Y88b._ --')
print('--  88888P_Y88888_888____888_888__Y8P__888_______"888_ --')
print('--  8888P___Y8888_Y88b__d88P_888___"___888_Y88b__d88P_ --')
print('--  888P_____Y888__"Y8888P"__888_______888__"Y8888P"__ --')
print('--  __________________________________________________ --')
import mysql.connector
m_con=mysql.connector.connect(host='localhost',user='root',password='password')
m_cur=m_con.cursor()
m_cur.execute('CREATE DATABASE if not exists WMS')
m_cur.execute('USE WMS')
m_cur.execute('create table if not exists sector_w(sec_id int not null,worker_id int primary key not null,worker_name varchar(255)not null,w_address varchar(255) not null,w_phno int unique)')
m_cur.execute('create table if not exists sector_h(house_id int primary key not null,address varchar(255) unique not null,resident_name varchar(255) not null,resident_phno int unique, sec_id int not null)')
m_cur.execute("create table if not exists record(date varchar(12) not null,house_id int primary key not null,w_coll_status varchar(255) default 'not collected',pay_amount-INR varchar(255) not null default 20, pay_status varchar(255) default 'unpaid')")
m_con.commit()
m_con.close()
print('Tables created successfully')
def ed_w():
    m_con=mysql.connector.connect(host='localhost',user='root',password='password')
    m_cur=m_con.cursor()
    m_cur.execute('use WMS')
    while True:
        c_s=int(input('1.Add new worker \n2.Edit details \n3.Delete data \n4.Exit'))
        if c_s==1:
            w1=int(input('enter sector id:'))
            w2=int(input('enter worker_id:'))
            w3=input('enter worker_name:')
            w4=input('residence address:')
            w5=int(input('contact no.'))
            m_cur.execute('use WMS')
            m_cur.execute('insert into table sector_w values({},{},"{}","{}",{})'.format(w1,w2,w3,w4,w5))
            m_con.commit()
            print('Values inserted successfully')
        elif c_s==2:
            m_cur.execute('use WMS')
            c_s2=int(input('1.Change residence address \n2.Change contact no.'))
            if c_s2==1:
                sid=int(input('Enter worker id'))
                a=input('Enter address:')
                cm='update sector_w set w_address={} where worker_id={}'.format(a,sid)
                m_cur.execute(cm)
                m_con.commit()
                print('Changes inserted successfully')
            elif c_s2==2:
                sid=int(input('Enter worker id'))
                con=input('Enter contact no.')
                cm='update sector_w set w_phno.(+91)={} where worker_id={}'.format(con,sid)
                m_cur.execute(cm)
                m_con.commit()
                print('Changes inserted successfully')
        elif c_s==3:
            sid=int(input('Enter worker id'))
            cm='delete from sector_w where worker_id={}'.format(sid)
            m_cur.execute(cm)
            m_con.commit()
            print('Changes inserted successfully')
        elif c_s==4:
            print('exit')
            break
def ed_h():
    m_con=mysql.connector.connect(host='localhost',user='root',password='password')
    m_cur=m_con.cursor()
    m_cur.execute('use WMS')
    while True:
        c_h=int(input('1.Add new house \n2.Edit details \n3.Delete data \n4.Exit'))
        m_cur.execute('use WMS')
        if c_h==1:
            h1=int(input('enter house id:'))
            h2=input('enter address:')
            h3=input('enter resident name:')
            h4=int(input('enter sector id:'))
            h5=int(input('enter resedent phone no.'))
            m_cur.execute('insert into table sector_h values({}),"{}","{}".{},{})'.format(h1,h2,h3,h5,h4))
            m_con.commit()
            print('Values inserted successfully')
        elif c_h==2:
            c_h2=int(input('1.Change residence address \n2.Change contact no. \n2.Change resident name'))
            hid=int(input('Enter house id'))
            if c_h2==1:
                a=input('Enter address:')
                cm='update sector_h set address={} where house_id={}'.format(a,hid)
                m_cur.execute(cm)
                m_con.commit()
                print('Changes inserted successfully')
            elif c_h2==2:
                n=int(input('Enter phone no.'))
                cm='update sector_h set resident_phno={} where house_id={}'.format(n,hid)
                m_cur.execute(cm)
                m_con.commit()
                print('Changes inserted successfully')
            elif c_h==3:
                hid=int(input('Enter house id'))
                cm='delete from sector_h where house_id={}'.format(hid)
                m_cur.execute(cm)
                m_con.commit()
                print('Changes inserted successfully')
            elif c_h==4:
                print('exit')
                break
def ed_r():
    m_con=mysql.connector.connect(host='localhost',user='root',password='password')
    m_cur=m_con.cursor()
    m_cur.execute('use WMS')
    while True:
        c_r=int(input('1.Enter new data \n2.Update payment status \n3.Update waste collection status \n4.Exit:'))
        if c_r==1:
            r0=input('Enter date(dd/mm/yyyy):')
            r1=int(input('enter house id:'))
            r2=input('enter waste collection status(collected/not collecter):')
            r3=int(input('enter amount to be paid:'))
            r4=input('enter payment status(paid/unpaid):')
            m_cur.execute("insert into table record values('{}',{},'{}',{},'{}')".format(r0,r1,r2,r3,r4))
            m_con.commit()
            print('Values inserted successfully')
        elif c_r==2:
            hid=int(input('Enter house id'))
            st=input('Enter payment status(paid/unpaid):')
            cm='update record set pay_status(INR)={} where house_id={}'.format(st,hid)
            m_cur.execute(cm)
            m_con.commit()
            print('Changes inserted successfully')
        elif c_r==3:
            hid=int(input('Enter house id'))
            st=input('Enter waste collection status(collected/not collected):')
            cm='update record set w_coll_status(collected/not collected)={} where house_id={}'.format(st,hid)
            m_cur.execute(cm)
            m_con.commit()
            print('Changes inserted successfully')
        elif c_r==4:
            print('exit')
            break
def sh_w():
    m_con=mysql.connector.connect(host='localhost',user='root',password='password')
    m_cur=m_con.cursor() 
    m_cur.execute('use WMS')
    m_cur('select * from sector_w')
    row=m_cur.fetchall()
    print('Sector\t\t Worker ID\t\t Worker Name\t\t Worker Address \t\tWorker Phone no.')
    for r in row:
        print(r[0],'\t\t', r[1],'\t\t', r[2],'\t\t', r[3],'\t\t', r[4])
def sh_h():
    m_con=mysql.connector.connect(host='localhost',user='root',password='password')
    m_cur=m_con.cursor() 
    m_cur.execute('use WMS')
    m_cur('select * from sector_h')
    row=m_cur.fetchall()
    print('House id\t\t Address\t\t Resident Name\t\t Resdient Phone no. \t\t Sector')
    for r in row:
        print(r[0],'\t\t' ,r[1],'\t\t' ,r[2],'\t\t' ,r[3],'\t\t' ,r[4],'\t\t')
def sh_r():
    m_con=mysql.connector.connect(host='localhost',user='root',password='password')
    m_cur=m_con.cursor() 
    m_cur.execute('use WMS')
    m_cur('select * from record')
    row=m_cur.fetchall()
    print('Date\t\t House ID\t\t Waste Collection status\t\t Payment Amount\t\t Payment Status')
    for r in row:
        print(r[0],'\t\t',r[1],'\t\t',r[2],'\t\t',r[3],'\t\t')
while True:
    print('1.Sector Worker\n 2.Sector House\n 3.Record')
    c=int(input('Enter choice:'))
    if c==1:
        c2=int(input('1.edit \n2.show \nEnter choice:'))
        if c2==1:
            ed_w()
        elif c2==2:
            sh_w()
    elif c==2:
        c2=int(input('1.edit \n2.show \nEnter choice:'))
        if c2==1:
            ed_h()
        elif c2==2:
            sh_h()
    elif c==3:
        c2=int(input('1.edit \n2.show \nEnter choice:'))
        if c2==1:
            ed_r()
        elif c2==2:
            sh_r()
    else:
        print('Exit')
        break
