import tkinter as tk
from tkinter import font as tkfont

# Create main window
root = tk.Tk()
root.title("Stylish Calculator")
root.geometry("400x550")
root.configure(bg="#2e2e2e")
root.resizable(False, False)

# Global expression string
expression = ""

# Custom fonts
display_font = tkfont.Font(family="Helvetica", size=28, weight="bold")
button_font = tkfont.Font(family="Helvetica", size=18)

# Function to update expression
def press(symbol):
    global expression
    expression += str(symbol)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Function to clear the entry
def clear():
    global expression
    expression = ""
    equation.set("")

# Entry field
equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=display_font,
                 bg="#1e1e1e", fg="white", bd=0, justify='right')
entry.pack(expand=True, fill='both', ipady=20)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Function to create each row of buttons
for row_values in buttons:
    row = tk.Frame(root, bg="#2e2e2e")
    row.pack(expand=True, fill='both')
    for value in row_values:
        action = lambda x=value: equalpress() if x == '=' else press(x)
        tk.Button(row, text=value, font=button_font, fg="white", bg="#3b3b3b", bd=0,
                  activebackground="#5c5c5c", command=action).pack(side='left', expand=True, fill='both')

# Clear button row
clear_row = tk.Frame(root, bg="#2e2e2e")
clear_row.pack(expand=True, fill='both')
tk.Button(clear_row, text="C", font=button_font, fg="white", bg="#d9534f", bd=0,
          activebackground="#c9302c", command=clear).pack(side='left', expand=True, fill='both')

# Run app
root.mainloop()
