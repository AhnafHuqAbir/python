from tkinter import *
root = Tk()
root.title("Login App")
root.geometry("400x400")
frame = Frame(master = root, height = 200, width = 360, bg = "#d0efff")

lbl1 = Label(frame, text = "Full name", bg = "#3895d3", fg = "white", width = 12)
lbl2 = Label(frame, text = "Email", bg = "#3895d3", fg = "white", width = 12)
lbl3 = Label(frame, text = "Enter password", bg = "#3895d3", fg = "white", width = 12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show = ".")

def display():
    name = name_entry.get()
    greet = "Hellow" + name
    Message = "\nCongratulations! You have successfully logged in."
    textbox.insert(END, greet)
    textbox.insert(END, Message)

textbox = Text(bg = "#bebebe", fg = 'black')

btn = Button(text = "create account", command = display, bg = "red")

frame.place(x = 20, y = 0)
lbl1.place(x = 20, y = 20)
name_entry.place(x = 150, y = 20)
lbl2.place(x = 20, y = 80)
email_entry.place(x = 150, y = 80)
lbl3.place(x = 20, y = 140)
password_entry.place(x = 150, y = 140)
btn.place(x = 150, y = 200)
textbox.place(y = 250)

root.mainloop()