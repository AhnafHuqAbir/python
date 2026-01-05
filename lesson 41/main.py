from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open("app_img.jpg")
# Resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
               text="Hey User! Welcome to Denomination Counter Application.",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomtnation count?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root,
                 text = "Let,s get started!!!",
                 command = msg,
                 bg = "Brown",
                 fg = 'white')
button1.place(x = 260, y = 360)

def topwin():
    top = Toplevel()
    top.title('Denomination Counter')
    top.configure(bg = "DarkBlue")
    top.geometry("600x450")

    lable = Lable(top, text = "Enter the Amount :", bg = "Skyblue")
    entry = Entey(top)
    lbl = Label(top, text = "Here are the denomination counts :", bg = "Skyblue")

    lb1 = Label(top, text = "2000", bg = "grey")
    lb2 = Label(top, text = "500", bg = "grey")
    lb3 = Label(top, text = "100", bg = "grey")

    ti1 = Label(top)
    ti2 = Label(top)
    ti3 = Label(top)

    def calculate():
        try:
            global amount
            amount - int(entry.get())
            note2000 = amount // 2000
            amount = amount % 2000
            note500 = amount // 500
            amount = amount % 500
            note100 = amount // 100

            













    # Centering Widgets in the Top Window
    label.place(x=230, y=50   )
    entry.place(x=200, y=80   )
    btn.place(x=240, y=120   )
    lbl.place(x=140, y=170   )

    l1.place(x=180, y=200   )
    l2.place(x=180, y=230   )
    l3.place(x=180, y=260   )

    t1.place(x=270, y=200   )
    t2.place(x=270, y=230   )
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()
