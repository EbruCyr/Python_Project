import tkinter as tk
import math
import numpy as np
import matplotlib.pyplot as plt

PINK = "#FB607F"
LIGHT_PINK = "#FF91A4"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")

        # Create the colored display frame
        self.create_display_frame()
        # Create the button frame
        self.create_button_frame()

        self.entry = tk.Entry(self.display_frame, width=60, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        button_labels = [
            "1", "2", "3", "+",
            "4", "5", "6", "-",
            "7", "8", "9", "*",
            "0", ".", "/", "C",
            "=", "**", "%", "!",
            "sqrt", "|x|", "log", "log10"
        ]

        row = 1
        col = 0
        for label in button_labels:
            if label.isdigit() or label == ".":
                button = tk.Button(self.button_frame, text=label, padx=35, pady=25, bg=PINK)
                button.config(command=lambda num=label: self.button_click(num))
            elif label == "=":
                button = tk.Button(self.button_frame, text=label, padx=35, pady=25, bg=PINK)
                button.config(command=self.button_equal)
            elif label == "C":
                button = tk.Button(self.button_frame, text=label, padx=35, pady=25, bg=PINK)
                button.config(command=self.button_clear)
            elif label == "!":
                button = tk.Button(self.button_frame, text=label, padx=35, pady=25, bg=PINK)
                button.config(command=self.button_factorial)
            elif label == "sqrt":
                button = tk.Button(self.button_frame, text=label, padx=35, pady=25, bg=PINK)
                button.config(command=self.button_squareroot)
            elif label == "|x|":
                button = tk.Button(self.button_frame, text=label, padx=35, pady=25, bg=PINK)
                button.config(command=self.button_absolute)
            elif label == "log":
                button = tk.Button(self.button_frame, text=label, padx=35, pady=25, bg=PINK)
                button.config(command=self.button_logarithm)
            elif label == "log10":
                button = tk.Button(self.button_frame, text=label, padx=35, pady=25, bg=PINK)
                button.config(command=self.button_logarithm_10)
            else:
                button = tk.Button(self.button_frame, text=label, padx=35, pady=25, bg=PINK)
                button.config(command=lambda op=label: self.button_click(op))

            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.window.mainloop()

    def button_click(self, number):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current + str(number))

    def button_clear(self):
        self.entry.delete(0, tk.END)

    def button_equal(self):
        result = eval(self.entry.get())
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, result)

    def button_squareroot(self):
        value = self.entry.get()
        if value:
            try:
                number = float(value)
                square = math.sqrt(number)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, square)
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Invalid statement")

    def button_factorial(self):
        value = self.entry.get()
        if value:
            try:
                number = int(value)
                factorial = math.factorial(number)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, factorial)
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Invalid statement")

    def button_absolute(self):
        value = self.entry.get()
        if value:
            try:
                number = int(value)
                absolute = math.fabs(number)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, absolute)
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Invalid statement")

    def button_logarithm(self):
        value = self.entry.get()
        if value:
            try:
                number = float(value)
                logarithm = math.log(number)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, logarithm)
                self.plot_log(number, logarithm)
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Invalid statement")

    def button_logarithm_10(self):
        value = self.entry.get()
        if value:
            try:
                number = float(value)
                logarithm = math.log10(number)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, logarithm)
                self.plot_log(number, logarithm)
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Invalid statement")

    # display logarithm graph
    def plot_log(self, value, result):
        x = np.linspace(0.1, 10, 100)
        y = np.vectorize(lambda x: math.log(x))(x)

        plt.figure()
        plt.plot(x, y)
        plt.scatter(value, result, color='red', label='Log({})'.format(value))
        plt.xlabel('x')
        plt.ylabel('log(x)')
        plt.title('Logarithms Graph')
        plt.legend()
        plt.grid(True)
        plt.show()

    def create_display_frame(self):
        self.display_frame = tk.Frame(self.window, height=100, bg=LIGHT_PINK)
        self.display_frame.pack(expand=True, fill="both")

    def create_button_frame(self):
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(expand=True, fill="both")

calculator = Calculator()
