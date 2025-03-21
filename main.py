import tkinter as tk
from tkinter import messagebox


def calculate_bill():
    try:
        units = float(entry_units.get())
        if units <= 0:
            raise ValueError("Units must be positive")

        #
        if units <= 100:
            bill = units * 1.5
        elif units <= 200:
            bill = (100 * 1.5) + ((units - 100) * 2.5)
        elif units <= 300:
            bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 3.0)
        else:
            bill = (100 * 1.5) + (100 * 2.5) + (100 * 3.0) + ((units - 300) * 5.0)


        label_result.config(text=f"Total Bill: ₹{bill:.2f}")

    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")



root = tk.Tk()
root.title("Electricity Bill System")


label_title = tk.Label(root, text="Electricity Bill Calculator", font=("Arial", 16))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

label_units = tk.Label(root, text="Enter Units Consumed:")
label_units.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_units = tk.Entry(root)
entry_units.grid(row=1, column=1, padx=10, pady=10)

button_calculate = tk.Button(root, text="Calculate Bill", command=calculate_bill)
button_calculate.grid(row=2, column=0, columnspan=2, pady=20)

label_result = tk.Label(root, text="Total Bill: ₹0.00", font=("Arial", 14))
label_result.grid(row=3, column=0, columnspan=2)


root.mainloop()
