from tkinter import *
from tkinter.filedialog import asksaveasfile
window = Tk()
window.geometry("200x100")
def save():
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)

btn = Button(window, text = "save as", command = lambda: save())
btn.pack(side = TOP)

mainloop()