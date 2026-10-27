import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()

mycursor.execute("create database if not exists pythonform")
mydb.commit()

mydb=pymysql.connect(host="localhost",user="root",password="",database="pythonform")
mycursor=mydb.cursor()

mycursor.execute("create table if not exists form (id int primary key auto_increment,name varchar(60),mobile bigint ,email varchar(60),password varchar(50),c_password varchar(50))")
mydb.commit()