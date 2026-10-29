from tkinter import *

root = Tk()
root.title("Music Buttons")
root.geometry("400x300")

Button(root, text="Like").place(x=80, y=50)
Button(root, text="Share").place(x=200, y=50)
Button(root, text="Download").place(x=80, y=120)
Button(root, text="Add to Queue").place(x=200, y=120)

root.mainloop()