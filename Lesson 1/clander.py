import tkinter as tk
import calendar
from tkinter import ttk

# Function to show calendar of selected month/year
def show_calendar():
    try:
        month = int(month_entry.get())
        year = int(year_entry.get())
        cal_text = calendar.month(year, month)
        cal_output.delete(1.0, tk.END)
        cal_output.insert(tk.END, cal_text)
    except:
        cal_output.delete(1.0, tk.END)
        cal_output.insert(tk.END, "Invalid Input")

# Main window
root = tk.Tk()
root.title("Simple Calendar")
root.geometry("400x400")
root.configure(bg="#2e2e2e")

# Labels and entry fields
tk.Label(root, text="Year:", font=("Helvetica", 14), bg="#2e2e2e", fg="white").pack(pady=5)
year_entry = tk.Entry(root, font=("Helvetica", 14), justify='center')
year_entry.pack(pady=5)

tk.Label(root, text="Month (1-12):", font=("Helvetica", 14), bg="#2e2e2e", fg="white").pack(pady=5)
month_entry = tk.Entry(root, font=("Helvetica", 14), justify='center')
month_entry.pack(pady=5)

# Show Calendar Button
ttk.Button(root, text="Show Calendar", command=show_calendar).pack(pady=10)

# Output display area
cal_output = tk.Text(root, height=10, width=30, font=("Courier", 14), bg="#1e1e1e", fg="white", bd=0)
cal_output.pack(pady=10)

# Run the app
root.mainloop()
