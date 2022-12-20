#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:33:20 2022

@author: sooryankc
"""
import mysql
m_con=mysql.connector.connector( #connection
    host='localhost',
    user='root',
    password='french'
    )
m_cur=m_con.cursor()   #cursor
m_cur.execute('create database WMS')
m_cur.execute('create table sector_w(sec_id int not null, worker_id int primary key not null, worker_name varchar(655)not null, w_address varchar(60000) not null,w_phno.(+91) int unique)')
m_cur.execute('create table sector_h(house_id int primary key not null,address varchar(60000) unique not null,resident name varchar(255) not null,resident_phno.(+91) int unique,sec_id int not null)')
m_cur.execute("create table record(house_id int primary key not null,w_coll_status(collected/not collected) varchar(255) default 'not collected', pay_amount varchar(255) not null, pay_status(INR) varchar(255) default'unpaid')")
m_con.commit()
m_con.close()
print('Tables created successfully')
def ed_w():
    	m_con=mysql.connector.connector( #connection
        	host='localhost',
        	user='root',
        	password='french'
        	)
    	m_cur=m_con.cursor()   #cursor
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
	m_con=mysql.connector.connector( #connection
       		host='localhost',
       		user='root',
       		password='french'
       		)
    	m_cur=m_con.cursor()   #cursor
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
                		cm='update sector_h set resident_phno.(+91)={} where house_id={}'.format(n,hid)
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
	m_con=mysql.connector.connector(                                    #connection
       		host='localhost',
        	user='root',
        	password='french'
        	)
    	m_cur=m_con.cursor()                                                #cursor
	m_cur.execute('use WMS')
    	while True:
		c_r=int(input('1.Enter new data \n2.Update payment status \n3.Update waste collection status \n4.Exit:'))
		if c_r==1:
			r1=int(input('enter house id:'))
    			r2=input('enter waste collection status(collected/not collecter):')
    			r3=int(input('enter amount to be paid:'))
    			r4=input('enter payment status(paid/unpaid):')
    			m_cur.execute('insert into table record values({},"{}".{},"{}")'.format(r1,r2,r3,r4))
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
	m_con=mysql.connector.connector(                                    #connection
        	host='localhost',
        	user='root',
        	password='french'
		)
	m_cur=m_con.cursor() 
	m_cur.execute('use WMS')
	m_cur('select * from sector_w')
	row=m_cur.fetchall()
	print('Sector\t\t Worker ID\t\t Worker Name\t\t Worker Address \t\tWorker Phone no.')
	for r in row:
		print(r[0]\t\t r[1]\t\t r[2]\t\t r[3]\t\t r[4]\t\t)
def sh_h():
	m_con=mysql.connector.connector(                                    #connection
        	host='localhost',
        	user='root',
        	password='french'
		)
	m_cur=m_con.cursor() 
	m_cur.execute('use WMS')
	m_cur('select * from sector_h')
	row=m_cur.fetchall()
	print('House id\t\t Address\t\t Resident Name\t\t Resdient Phone no. \t\t Sector')
	for r in row:
		print(r[0]\t\t r[1]\t\t r[2]\t\t r[3]\t\t r[4]\t\t)
def sh_r():
	m_con=mysql.connector.connector(                                    #connection
        	host='localhost',
        	user='root',
        	password='french'
		)
	m_cur=m_con.cursor() 
	m_cur.execute('use WMS')
	m_cur('select * from record')
	row=m_cur.fetchall()
	print('House ID\t\t Waste Collection status\t\t Payment Amount\t\t Payment Status')
	for r in row:
		print(r[0]\t\t r[1]\t\t r[2]\t\t r[3]\t\t)
while True:
    print('1.Sector Worker\n 2.Sector House\n 3.Record')
    c=int(input('Enter choice:'))
    if c==1:
        c2=int(input('1.edit \n2.show'))
	       if c2==1:
			ed_w()
		elif c2==2:
			sh_w()
    elif c==2:
        c2=int(input('1.edit \n2.show'))
	       if c2==1:
			ed_h()
		elif c2==2:
			sh_h()
    elif c==3:
        c2=int(input('1.edit \n2.show'))
	       if c2==1:
			ed_r()
		elif c2==2:
			sh_r()
    else:
        print('Exit')
        break
