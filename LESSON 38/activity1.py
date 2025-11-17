from tkinter import *
window = Tk()
window.title("Simple frame")
window.geometry("500x400")

border_effects = [FLAT, SUNKEN, RAISED, GROOVE, RIDGE]

for i in border_effects:
    frame = Frame(master = window, relief = i, borderwidth = 5)
    frame.pack(side = LEFT)
    label = Label(master = frame, text = i)
    label.pack()
window.mainloop()