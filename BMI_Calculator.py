import tkinter as tk
from tkinter import messagebox
import csv
import os

# -------- BMI Calculation --------
def calculate_bmi():
    try:
        name = entry_name.get().strip()
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())

        if name == "":
            messagebox.showwarning("Input Error", "Please enter your name")
            return

        if weight <= 0 or height_cm <= 0:
            messagebox.showwarning("Input Error", "Height and Weight must be positive")
            return

        height = height_cm / 100
        bmi = round(weight / (height ** 2), 2)

        # Category Logic
        if bmi < 18.5:
            category = "Underweight"
            color = "#3498db"
            tip = "Eat more nutritious food 🍎"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
            color = "#2ecc71"
            tip = "Great! Maintain your lifestyle 💪"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "#f39c12"
            tip = "Exercise regularly 🏃"
        else:
            category = "Obese"
            color = "#e74c3c"
            tip = "Consult a doctor & follow diet 🩺"

        result_label.config(
            text=f"{name}, your BMI is {bmi}\nCategory: {category}\n{tip}",
            fg=color
        )

        save_to_csv(name, weight, height_cm, bmi, category)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values")

# -------- Save Data --------
def save_to_csv(name, weight, height, bmi, category):
    file_exists = os.path.isfile("bmi_data.csv")

    with open("bmi_data.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Weight(kg)", "Height(cm)", "BMI", "Category"])

        writer.writerow([name, weight, height, bmi, category])

# -------- GUI --------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x450")
root.config(bg="#1e1e2f")

# Title
tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=15)

# Name
tk.Label(root, text="Name", bg="#1e1e2f", fg="white").pack()
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.pack(pady=5)

# Weight
tk.Label(root, text="Weight (kg)", bg="#1e1e2f", fg="white").pack()
entry_weight = tk.Entry(root, font=("Arial", 12))
entry_weight.pack(pady=5)

# Height
tk.Label(root, text="Height (cm)", bg="#1e1e2f", fg="white").pack()
entry_height = tk.Entry(root, font=("Arial", 12))
entry_height.pack(pady=5)

# Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi,
          bg="#4CAF50", fg="white", font=("Arial", 12), width=20).pack(pady=20)

# Result
result_label = tk.Label(root, text="", bg="#1e1e2f",
                        fg="white", font=("Arial", 12),
                        wraplength=300, justify="center")
result_label.pack(pady=20)

root.mainloop()
