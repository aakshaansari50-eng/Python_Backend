from tkinter import *

def login():
    root=Tk()
    root.geometry("500x500")
    root.title("Login Page")
    
    email=Label(root,text="Enter Email",font=("Calibri",14,"bold"))
    email.place(x=50,y=100)
    
    password=Label(root,text="Enter Password",font=("Calibri",14,"bold"))
    password.place(x=50,y=150)
    
    cpassword=Label(root,text="Enter Password",font=("Calibri",14,"bold"))
    cpassword.place(x=50,y=200)
    
    email=Entry(root,bg="lightblue")
    email.place(x=280,y=105)
    
    password=Entry(root,bg="lightblue")
    password.place(x=280,y=155)
        
    cpassword=Entry(root,bg="lightblue")
    cpassword.place(x=280,y=205)
    
    Submit=Button(root,fg="red",font=("Calibri",18,"italic"),text="Submit")
    Submit.place(x=50,y=250)
    
    root.mainloop()

    
