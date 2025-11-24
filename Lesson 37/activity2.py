from tkinter import*
from datetime import datetime

root = Tk()
root.title("Getting started with Widgets")
root.geometry("500x400")

# lable 
lb1 = Label(text = "Hellow!!!", fg = "gray", bg = "#000000", height= 1, width = 300)

name_lb1 = Label(text = "Enter your name: ", bg = "lightblue")
name_entry = Entry()

def display():
    name = name_entry.get()
    massage = "wellcome to the world of python \n Today's date is: "
    greet = f"Hay {name} \n"

    text_box.insert(END, greet)
    text_box.insert(END, massage)
    text_box.insert(END, datetime.now().date())

text_box = Text(height = 3)

btn = Button(text = "Begin", command = display, height = 1, bg = "lightgreen", fg = "black")
lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
