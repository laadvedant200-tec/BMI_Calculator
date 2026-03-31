import tkinter as tk
from tkinter import messagebox
import csv
import os

# ---------- BMI Calculation Logic ----------
def calculate_bmi():
    try:
        user_name = name_input.get().strip()
        user_weight = float(weight_input.get())
        user_height_cm = float(height_input.get())

        # Basic validation
        if not user_name:
            messagebox.showwarning("Missing Info", "Hey! Please enter your name 😊")
            return

        if user_weight <= 0 or user_height_cm <= 0:
            messagebox.showwarning("Invalid Input", "Height and weight must be greater than 0")
            return

        # BMI Formula
        height_in_m = user_height_cm / 100
        bmi_value = round(user_weight / (height_in_m ** 2), 2)

        # BMI Category Decision
        if bmi_value < 18.5:
            category = "Underweight"
            color = "#3498db"
            suggestion = "Try to eat more nutritious food 🍎"
        elif bmi_value < 24.9:
            category = "Normal"
            color = "#2ecc71"
            suggestion = "You're doing great! Keep it up 💪"
        elif bmi_value < 29.9:
            category = "Overweight"
            color = "#f39c12"
            suggestion = "Consider regular exercise 🏃"
        else:
            category = "Obese"
            color = "#e74c3c"
            suggestion = "Better consult a doctor & improve diet 🩺"

        # Show result nicely
        result_display.config(
            text=f"Hi {user_name}!\n\nYour BMI is: {bmi_value}\nCategory: {category}\n\n{suggestion}",
            fg=color
        )

        # Save data
        save_data(user_name, user_weight, user_height_cm, bmi_value, category)

    except ValueError:
        messagebox.showerror("Input Error", "Only numbers are allowed for height and weight!")

# ---------- Save Data to CSV ----------
def save_data(name, weight, height, bmi, category):
    file_name = "bmi_records.csv"
    file_exists = os.path.isfile(file_name)

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)

        # Add header if file is new
        if not file_exists:
            writer.writerow(["Name", "Weight (kg)", "Height (cm)", "BMI", "Category"])

        writer.writerow([name, weight, height, bmi, category])

# ---------- GUI Design ----------
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("420x480")
app.config(bg="#1e1e2f")

# Title
tk.Label(app, text="BMI Calculator",
         font=("Arial", 20, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=15)

# Name Input
tk.Label(app, text="Your Name", bg="#1e1e2f", fg="white").pack()
name_input = tk.Entry(app, font=("Arial", 12))
name_input.pack(pady=5)

# Weight Input
tk.Label(app, text="Weight (kg)", bg="#1e1e2f", fg="white").pack()
weight_input = tk.Entry(app, font=("Arial", 12))
weight_input.pack(pady=5)

# Height Input
tk.Label(app, text="Height (cm)", bg="#1e1e2f", fg="white").pack()
height_input = tk.Entry(app, font=("Arial", 12))
height_input.pack(pady=5)

# Calculate Button
tk.Button(app,
          text="Calculate BMI",
          command=calculate_bmi,
          bg="#4CAF50",
          fg="white",
          font=("Arial", 12),
          width=20).pack(pady=20)

# Result Display
result_display = tk.Label(app,
                          text="",
                          bg="#1e1e2f",
                          fg="white",
                          font=("Arial", 12),
                          wraplength=320,
                          justify="center")
result_display.pack(pady=20)

# Run App
app.mainloop()
