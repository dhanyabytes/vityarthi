import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    """Calculates BMI based on user input and updates the result label."""
    try:
        # 1. Get user input and convert to float
        height_m = float(height_entry.get())
        weight_kg = float(weight_entry.get())

        # Input Validation (Essential for robust apps)
        if height_m <= 0 or weight_kg <= 0:
            messagebox.showerror("Input Error", "Height and Weight must be positive values greater than zero.")
            return

        # 2. Calculate BMI
        # Formula: weight / (height * height)
        bmi = weight_kg / (height_m ** 2)

        # Round BMI for a cleaner display
        bmi_rounded = round(bmi, 2)

        # 3. Determine Classification (Using the seamless, corrected logic)
        if bmi < 18.5:
            classification = "Underweight"
        elif bmi < 24.9: # Covers >= 18.5 AND < 24.9
            classification = "Normal Weight"
        elif bmi < 29.9: # Covers >= 24.9 AND < 29.9
            classification = "Overweight"
        else:            # Covers >= 29.9
            classification = "Obesity"

        # 4. Update the GUI result label
        result_text = (f"Your BMI is: {bmi_rounded}\n"
                       f"Classification: {classification}")

        # Update the label widget's text
        result_label.config(text=result_text, fg='blue')

    except ValueError:
        # Handle non-numeric input errors gracefully
        messagebox.showerror("Input Error", "Please enter valid numbers for Height and Weight.")


# --- Tkinter Setup ---
# 1. Create the main application window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250") # Set initial window size

# --- Widgets for Input ---

# Height Label and Entry
height_label = tk.Label(root, text="Height (Metres):")
height_label.pack(pady=5)
height_entry = tk.Entry(root, width=15)
height_entry.pack(pady=2)

# Weight Label and Entry
weight_label = tk.Label(root, text="Weight (Kilograms):")
weight_label.pack(pady=5)
weight_entry = tk.Entry(root, width=15)
weight_entry.pack(pady=2)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg='green', fg='white')
calculate_button.pack(pady=10)

# Result Display Label
result_label = tk.Label(root, text="Enter values and click Calculate.",
                        font=('Arial', 10, 'bold'))
result_label.pack(pady=5)

# 6. Start the main event loop
# This keeps the window open and responsive to user actions
root.mainloop()
