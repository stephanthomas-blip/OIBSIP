import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase

    if lower_var.get():
        characters += string.ascii_lowercase

    if number_var.get():
        characters += string.digits

    if symbol_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "Select at least one character type.")
        return

    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Enter a valid length.")
            return

    except ValueError:
        messagebox.showerror("Error", "Length must be a number.")
        return

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    check_strength(password)


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.config(text="Strength: Weak")
    elif score <= 4:
        strength_label.config(text="Strength: Medium")
    else:
        strength_label.config(text="Strength: Strong")


def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Warning", "Generate a password first.")


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x400")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Random Password Generator",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

length_frame = tk.Frame(root)
length_frame.pack(pady=10)

tk.Label(
    length_frame,
    text="Password Length:"
).pack(side=tk.LEFT)

length_entry = tk.Entry(length_frame, width=10)
length_entry.insert(0, "12")
length_entry.pack(side=tk.LEFT, padx=10)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Include Uppercase Letters",
    variable=upper_var
).pack(anchor="w", padx=50)

tk.Checkbutton(
    root,
    text="Include Lowercase Letters",
    variable=lower_var
).pack(anchor="w", padx=50)

tk.Checkbutton(
    root,
    text="Include Numbers",
    variable=number_var
).pack(anchor="w", padx=50)

tk.Checkbutton(
    root,
    text="Include Symbols",
    variable=symbol_var
).pack(anchor="w", padx=50)

tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    width=20
).pack(pady=20)

password_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)
password_entry.pack(pady=10)

tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    width=20
).pack(pady=10)

strength_label = tk.Label(
    root,
    text="Strength: ",
    font=("Arial", 12)
)
strength_label.pack(pady=10)

root.mainloop()