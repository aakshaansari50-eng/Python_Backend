from tkinter import *

root = Tk()
root.title("My Playlist")
root.geometry("400x300")

def play():
    label.config(text="Playing")

def pause():
    label.config(text="Paused")

def next_song():
    label.config(text="Next Song")

Button(root, text="Play", command=play).place(x=50, y=50)
Button(root, text="Pause", command=pause).place(x=150, y=50)
Button(root, text="Next", command=next_song).place(x=250, y=50)

label = Label(root, text="Select an action", font=("Arial", 14))
label.place(x=100, y=120)

root.mainloop()