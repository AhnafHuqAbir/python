from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Main Window")
l = Label(root, text = "This is the Main Window")

top = Toplevel()
top.geometry("200x200")
top.title("Top Level Window")
l2 = Label(top, text = "This is a Toplevel Window")
l.pack()
l2.pack()
root.mainloop()