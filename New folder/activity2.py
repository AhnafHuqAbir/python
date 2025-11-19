from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("300x400")

def handel_keyprees(event):
    print(event.char)
window.bind("<Key>", handel_keyprees)
def handel_click(event):
    print(f'the btn was clicked!')

button = Button(window, text="Click Me")
button.pack()
button.bind("<Button-1>", handel_click)

window.mainloop()
