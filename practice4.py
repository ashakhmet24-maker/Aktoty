import tkinter as tk
from tkinter import messagebox

def calculate():
    value = entry.get()

    # 1. Empty validation
    if value == "":
        messagebox.showerror("Input Error", "Please enter a number.")
        return

    # 2. Type validation
    try:
        number = float(value)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")
        return

    # 3. Range validation
    if number < 0:
        messagebox.showerror("Input Error", "Number cannot be negative.")
        return

    # Calculation
    result = number * 2
    result_label.config(text=f"Result: {result:.2f}", fg="green")


def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result:", fg="black")


def check_input(*args):
    if entry.get() == "":
        calc_button.config(state="disabled")
    else:
        calc_button.config(state="normal")


# Window setup
root = tk.Tk()
root.title("Improved Calculator")
root.geometry("300x200")

# Label
label = tk.Label(root, text="Enter a number:")
label.pack(pady=5)

# Entry
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var)
entry.pack(pady=5)

entry_var.trace_add("write", check_input)

# Buttons
calc_button = tk.Button(root, text="Calculate", command=calculate, state="disabled")
calc_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack(pady=5)

# Result
result_label = tk.Label(root, text="Result:")
result_label.pack(pady=10)

root.mainloop()