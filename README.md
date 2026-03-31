# ⚖️ BMI Calculator with Data Logging

A sleek, desktop-based **Body Mass Index (BMI)** calculator built with Python's Tkinter library. This application not only calculates your BMI and provides health suggestions but also logs every entry into a local CSV file for progress tracking.

---

## ✨ Features

* **Real-time Calculation:** Instantiantly calculates BMI based on weight (kg) and height (cm).
* **Health Insights:** Categorizes results (Underweight, Normal, Overweight, Obese) with color-coded feedback and actionable suggestions.
* **Persistent Storage:** Automatically saves user data to `bmi_records.csv`.
* **Input Validation:** Robust error handling for empty fields or non-numeric inputs.
* **Modern UI:** Dark-themed interface with clear typography and organized layout.

---

## 🛠️ Built With

* **Python 3.x**
* **Tkinter:** For the Graphical User Interface (GUI).
* **CSV Module:** For data persistence and record keeping.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.x installed on your machine. Tkinter is usually bundled with standard Python installations.

### Installation & Execution
1.  **Save the code:** Save the Python script as `bmi_calculator.py`.
2.  **Run the application:**
    ```bash
    python bmi_calculator.py
    ```

---

## 📊 Data Management
The application creates a file named `bmi_records.csv` in the same directory as the script. This allows you to track your history over time.

**Data Structure:**
| Name | Weight (kg) | Height (cm) | BMI | Category |
| :--- | :--- | :--- | :--- | :--- |
| Alex | 70 | 175 | 22.86 | Normal |

> [!IMPORTANT]
> If you have `bmi_records.csv` open in a program like Microsoft Excel, the app may show an error when trying to save new data. Close the CSV file to resume saving.

---

## 🧮 Formula Used
The application uses the standard metric BMI formula:

$$BMI = \frac{\text{weight (kg)}}{\text{height (m)}^2}$$

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).

---
*Created with ❤️ by Your Name*
