import tkinter as tk

def f_to_c():
    """Convert Fahrenheit to Celsius and update the Celsius entry."""
    try:
        f = float(f_entry.get())
        c = (f - 32) * 5 / 9
        c_entry.delete(0, tk.END)
        c_entry.insert(0, f"{c:.2f}")
    except ValueError:
        c_entry.delete(0, tk.END)
        c_entry.insert(0, "Invalid input")

def c_to_f():
    """Convert Celsius to Fahrenheit and update the Fahrenheit entry."""
    try:
        c = float(c_entry.get())
        f = c * 9 / 5 + 32
        f_entry.delete(0, tk.END)
        f_entry.insert(0, f"{f:.2f}")
    except ValueError:
        f_entry.delete(0, tk.END)
        f_entry.insert(0, "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# First row: labels
tk.Label(root, text="Fahrenheit").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Celsius").grid(row=0, column=1, padx=5, pady=5)

# Second row: entry fields
f_entry = tk.Entry(root)
f_entry.grid(row=1, column=0, padx=5, pady=5)
f_entry.insert(0, "32.0")  # initial Fahrenheit value

c_entry = tk.Entry(root)
c_entry.grid(row=1, column=1, padx=5, pady=5)
c_entry.insert(0, "0.0")   # initial Celsius value

# Third row: conversion buttons
f_to_c_button = tk.Button(root, text=">>>>", command=f_to_c)
f_to_c_button.grid(row=2, column=0, padx=5, pady=5)

c_to_f_button = tk.Button(root, text="<<<<", command=c_to_f)
c_to_f_button.grid(row=2, column=1, padx=5, pady=5)

# Start the Tkinter main loop
root.mainloop()
