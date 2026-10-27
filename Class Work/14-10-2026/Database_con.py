import pymysql

mydb=pymysql.connect(host='localhost',user='root',password='')
mycourser=mydb.cursor()

mycourser.execute("create database if not exists python830")
mydb.commit()

mydb=pymysql.connect(host='localhost',user='root',password='',database='python830')
mycourser=mydb.cursor()

mycourser.execute("create table if not exists python400 (id int primary key auto_increment,name varchar(60),mobile bigint)")
mydb.commit()


