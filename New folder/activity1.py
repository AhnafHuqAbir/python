from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x300")

def msg():
    messagebox.showwarning("Warning", "stop! virus found")

button = Button(root, text = "Scan for virus", command=msg)
button.place(x=50, y=100)
root.mainloop()