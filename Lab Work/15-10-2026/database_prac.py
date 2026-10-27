import pymysql

mydb=pymysql.connect(host='localhost',user='root',password='')
mycursor=mydb.cursor()

mycursor.execute("create database if not exists college")
mydb.commit()

mydb=pymysql.connect(host='localhost',user='root',password='',database='college')
mycursor=mydb.cursor()

mycursor.execute("create table if not exists student(stu_id int primary key auto_increment,stu_name varchar(60),stu_age int,city varchar(50),mobile_no bigint)")
mydb.commit()