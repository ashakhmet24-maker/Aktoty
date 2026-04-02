import tkinter as tk
from tkinter import messagebox

def calculate():
    name = name_entry.get()
    age_value = age_entry.get()

    # Validation
    if name == "" or age_value == "":
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        age = int(age_value)
    except ValueError:
        messagebox.showerror("Error", "Age must be a number.")
        return

    if age < 0:
        messagebox.showerror("Error", "Age cannot be negative.")
        return

    # Result
    result_label.config(text=f"{name}, you are {age} years old!", fg="green")


def clear():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    result_label.config(text="Result:", fg="black")


# Window
root = tk.Tk()
root.title("User Form")
root.geometry("350x250")

# 🔹 Frame for input
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Name
name_label = tk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Age
age_label = tk.Label(input_frame, text="Age:")
age_label.grid(row=1, column=0, padx=5, pady=5)

age_entry = tk.Entry(input_frame)
age_entry.grid(row=1, column=1, padx=5, pady=5)

# 🔹 Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

calc_button = tk.Button(button_frame, text="Submit", command=calculate)
calc_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear)
clear_button.grid(row=0, column=1, padx=10)

# 🔹 Frame for result
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="Result:")
result_label.pack()

root.mainloop()