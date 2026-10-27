from database_prac import *

mydb=pymysql.connect(host='localhost',user='root',password='',database='college')
mycursor=mydb.cursor()

while True:
    menu="""
    press 1 for Insert Data
    press 2 for Update Data
    press 3 for Delete Data
    press 4 for Fetch Data
    Press 5 for Exit
    """
    print(menu)
    choice=int(input("Enter a Choice : "))
    
    if choice==1:
        name=input("Enter a Name : ")
        age=int(input("Enter Age : "))
        city=input("Enter City : ")
        mobile=int(input("Enter Mobile : "))
        
        query="insert into student(stu_name,stu_age,city,mobile_no) values ('%s','%s','%s','%s')"
        args=(name,age,city,mobile)
        
        mycursor.execute(query % args)
        mydb.commit()
        print("Data Inserted Succesfully!!")
        
    elif choice==2:
        id=int(input("Enter ID : "))
        name=input("Enter a Name : ")
        age=int(input("Enter Age : "))
        city=input("Enter City : ")
        mobile=int(input("Enter Mobile : "))
        
        query="update student set stu_name='%s',stu_age='%s',city='%s',mobile_no='%s' where stu_id='%s'"
        args=(name,age,city,mobile,id)
        
        mycursor.execute(query % args)
        mydb.commit()
        print("Data Updated Successfully!!")
        
    elif choice==3:
        id=int(input("Enter ID : "))
        
        query="delete from student where stu_id='%s'"
        args=(id)
        
        mycursor.execute(query % args)
        mydb.commit()
        print("Data Deleted Successfully")
        
    elif choice==4:
        query="select * from student"
        
        mycursor.execute(query)
        data=mycursor.fetchall()
        print(data)
        
    elif choice==5:
        print("Exit!!")
        
    else:
        print("Invalid Choice!!")