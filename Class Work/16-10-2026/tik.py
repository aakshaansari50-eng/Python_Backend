from tkinter import *
from loginpage import login
from pythonform_db import *

root=Tk()

root.geometry("500x500")
root.title("Registration Form")

id=Label(root,text="Enter ID  ",font=("calibri",14,"bold"))
id.place(x=50,y=50)

name=Label(root,text="Enter Name  ",font=("calibri",14,"bold"))
name.place(x=50,y=100)

email=Label(root,text="Enter Email  ",font=("calibri",14,"bold"))
email.place(x=50,y=150)

Mobile=Label(root,text="Enter Mobile  ",font=("calibri",14,"bold"))
Mobile.place(x=50,y=200)

password=Label(root,text="Enter Password  ",font=("calibri",14,"bold"))
password.place(x=50,y=250)

cpassword=Label(root,text="Enter Cpassword ",font=("calibri",14,"bold"))
cpassword.place(x=50,y=300)

eid=Entry(root,bg="skyblue")
eid.place(x=280,y=55)

ename=Entry(root,bg="skyblue")
ename.place(x=280,y=105)

eemail=Entry(root,bg="skyblue")
eemail.place(x=280,y=155)

emobile=Entry(root,bg="skyblue")
emobile.place(x=280,y=205)

epassword=Entry(root,bg="skyblue")
epassword.place(x=280,y=255)

ecpassword=Entry(root,bg="skyblue")
ecpassword.place(x=280,y=305)


mydb=pymysql.connect(host="localhost",user="root",password="",database="pythonform")
mycursor=mydb.cursor()

def Insert_data():
    name=ename.get()
    mobile=emobile.get()
    email=eemail.get()
    password=epassword.get()
    c_password=ecpassword.get()
        
    query="insert into form (name,mobile,email,password,c_password) values ('%s','%s','%s','%s','%s')"
    args=(name,mobile,email,password,c_password)
        
    mycursor.execute(query % args)
    mydb.commit()
    print("Data Inserted Successfully!!")

insert=Button(root,fg="red",font=("Calibri",18,"italic"),text="Insert",command=Insert_data)
insert.place(x=50,y=340)

def Update_data():
    id=eid.get()
    name=ename.get()
    mobile=emobile.get()
    email=eemail.get()
    password=epassword.get()
    c_password=ecpassword.get()
    query="update form set name='%s',mobile='%s',email='%s',password='%s',c_password='%s' where id='%s'"
    args=(name,mobile,email,password,c_password,id)
        
    mycursor.execute(query % args)
    mydb.commit()
    print("Data Updated Successfully!!")

update=Button(root,fg="red",font=("Calibri",18,"italic"),text="Update" ,command=Update_data)
update.place(x=140,y=340)

def Delete_data():
    id=eid.get()
    query="delete from form where id='%s'"
    args=(id)
        
    mycursor.execute(query % args)
    mydb.commit()
    print("Data Deleted Successfully!!")

delete=Button(root,fg="red",font=("Calibri",18,"italic"),text="Delete" ,command=Delete_data)
delete.place(x=250,y=340)

def Search_data():
    query="select * from form"
        
    mycursor.execute(query)
    data=mycursor.fetchall()
    print(data)

search=Button(root,fg="red",font=("Calibri",18,"italic"),text="Search",command=Search_data)
search.place(x=350,y=340)

root.mainloop()

