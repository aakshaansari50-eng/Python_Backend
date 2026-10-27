from Database_con import *

mydb=pymysql.connect(host='localhost',user='root',password='',database='python830')
mycourser=mydb.cursor()

while True:
    menu="""
    press 1 for Insert Data
    press 2 for Update Data
    press 3 for Delete Data
    press 4 for Fetch Data
    press 5 for Exit
    """
    print(menu)
    choice=int(input("Enter Choice : "))
    
    if choice==1:
        name=input("Enter Name : ")
        mobile=int(input("Enter Mobile : "))
        
        query="insert into python400 (name,mobile) values ('%s','%s')"
        args=(name,mobile)
        
        mycourser.execute(query % args)
        mydb.commit()
        print("Data Inserted!!")
        
    elif choice==2:
        id=int(input("Enter ID : "))
        name=input("Enter Name : ")
        mobile=int(input("Enter Mobile : "))
        
        query="update python400 set name='%s', mobile='%s' where id='%s'"
        args=(name,mobile,id)
        
        mycourser.execute(query % args)
        mydb.commit()
        print("Data Updated!!")
        
    elif choice==3:
        id=int(input("Enter ID : "))
    
        query="delete from python400 where id='%s'"
        args=(id)
        
        mycourser.execute(query % args)
        mydb.commit()
        print("Data Deleted!!")
        
    elif choice==4:
        query="select * from python400"
        
        mycourser.execute(query)
        data=mycourser.fetchall()
        print(data)
        
    elif choice==5:
        print("Exit!!")
        
    else:
        print("Bye!!")
        