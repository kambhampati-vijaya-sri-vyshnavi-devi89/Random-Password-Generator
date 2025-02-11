import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password based on selected complexity and length
def generate():
    try:
        length = int(length_entry.get())  # Get the length from the input field
        if length < 8:  # Minimum length check
            messagebox.showwarning("Input Error", "Password length should be at least 8 characters.")
            return
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number for password length.")
        return

    # Determine character set based on selected complexity
    if complexity_var.get() == 1:
        characters = string.ascii_letters  # Letters only
    elif complexity_var.get() == 2:
        characters = string.ascii_letters + string.digits  # Letters + digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation  # Full complexity

    password = ''.join(random.choice(characters) for i in range(length))

    # Display the generated password
    password_label.config(text=f"Generated Password: {password}")
    copy_button.config(state="normal")  # Enable the copy button

# Copy the password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(password_label.cget("text").replace("Generated Password: ", ""))  # Append password
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Clear the generated password and reset the input field
def clear():
    password_label.config(text="Generated Password: ")
    length_entry.delete(0, tk.END)
    length_entry.insert(0, "12")  # Reset to default length
    copy_button.config(state="disabled")  # Disable the copy button

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set up the layout with grid
root.geometry("400x300")

# Add a label to show the generated password
password_label = tk.Label(root, text="Generated Password: ", font=("Helvetica", 12), anchor="w")
password_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="w")

# Input for password length
length_label = tk.Label(root, text="Enter password length (minimum 8):", font=("Helvetica", 10))
length_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

length_entry = tk.Entry(root, font=("Helvetica", 10))
length_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
length_entry.insert(0, "12")  # Default value is 12

# Password complexity options
complexity_var = tk.IntVar(value=3)  # Default: full complexity

complexity_label = tk.Label(root, text="Select Password Complexity:", font=("Helvetica", 10))
complexity_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

complexity_1 = tk.Radiobutton(root, text="Letters Only", variable=complexity_var, value=1)
complexity_1.grid(row=2, column=1, padx=10, pady=5, sticky="w")

complexity_2 = tk.Radiobutton(root, text="Letters + Digits", variable=complexity_var, value=2)
complexity_2.grid(row=3, column=1, padx=10, pady=5, sticky="w")

complexity_3 = tk.Radiobutton(root, text="Full Complexity", variable=complexity_var, value=3)
complexity_3.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Generate password button
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12), command=generate)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=15)

# Copy to clipboard button (disabled initially)
copy_button = tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 12), command=copy_to_clipboard, state="disabled")
copy_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Clear button to reset everything
clear_button = tk.Button(root, text="Clear", font=("Helvetica", 12), command=clear)
clear_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
