import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Square Calculator")

        self.number_label = tk.Label(self.window, text="Enter a number:")
        self.number_label.pack(pady=5)

        self.number_entry = tk.Entry(self.window)
        self.number_entry.pack(pady=5)

        self.calculate_button = tk.Button(
            self.window,
            text="Calculate Square",
            command=self.on_button_click
        )
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(self.window, text="Result: ")
        self.result_label.pack(pady=5)

        self.window.mainloop()

    def validate_input(self, user_input):
        if user_input.strip() == "":
            messagebox.showerror("Input Error", "Please enter a value.")
            return None

        try:
            return float(user_input)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return None

    def calculate_square(self, number):
        return number * number

    def on_button_click(self):
        value = self.number_entry.get()
        number = self.validate_input(value)

        if number is not None:
            result = self.calculate_square(number)
            self.result_label.config(text="Result: " + str(result))


# Run the app
CalculatorApp()