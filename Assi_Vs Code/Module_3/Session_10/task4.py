from tkinter import *

root = Tk()
root.title("Login Form")
root.geometry("400x300")

Label(root, text="Username").place(x=50, y=40)
username = Entry(root)
username.place(x=150, y=40)

Label(root, text="Password").place(x=50, y=90)
password = Entry(root, show="*")
password.place(x=150, y=90)

def login():
    if username.get() != "" and password.get() != "":
        result.config(text="Login Successful")
    else:
        result.config(text="Please fill both fields")

Button(root, text="Login", command=login).place(x=150, y=140)

result = Label(root, text="")
result.place(x=120, y=190)

root.mainloop()