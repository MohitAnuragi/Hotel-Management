import tkinter as tk
from tkinter import messagebox
import os

# Helper function to check if the user database exists, and create it if not
def ensure_user_database():
    if not os.path.exists("user_database.txt"):
        with open("user_database.txt", "w") as file:
            file.write("admin,password\n")  # Default admin account

# Function to validate login
def login():
    username = username_var.get()
    password = password_var.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    ensure_user_database()

    with open("user_database.txt", "r") as file:
        users = file.readlines()

    for user in users:
        stored_username, stored_password = user.strip().split(",")
        if username == stored_username and password == stored_password:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            return

    messagebox.showerror("Login Failed", "Invalid Username or Password")

# Function to handle sign-up
def signup():
    def register_user():
        new_username = new_username_var.get()
        new_password = new_password_var.get()
        confirm_password = confirm_password_var.get()

        if new_username == "" or new_password == "" or confirm_password == "":
            messagebox.showerror("Error", "All fields are required", parent=signup_window)
            return

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match", parent=signup_window)
            return

        ensure_user_database()

        with open("user_database.txt", "r") as file:
            users = file.readlines()

        for user in users:
            stored_username, _ = user.strip().split(",")
            if new_username == stored_username:
                messagebox.showerror("Error", "Username already exists", parent=signup_window)
                return

        with open("user_database.txt", "a") as file:
            file.write(f"{new_username},{new_password}\n")

        messagebox.showinfo("Success", "Account created successfully", parent=signup_window)
        signup_window.destroy()

    # Sign-Up Window
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("400x400")
    signup_window.configure(bg="#ffffff")

    tk.Label(signup_window, text="Sign Up", font=("Arial", 24, "bold"), bg="#ffffff", fg="#333").pack(pady=20)

    tk.Label(signup_window, text="Username:", font=("Arial", 14), bg="#ffffff", fg="#333").pack(pady=5)
    new_username_var = tk.StringVar()
    tk.Entry(signup_window, textvariable=new_username_var, font=("Arial", 12), width=30).pack(pady=5)

    tk.Label(signup_window, text="Password:", font=("Arial", 14), bg="#ffffff", fg="#333").pack(pady=5)
    new_password_var = tk.StringVar()
    tk.Entry(signup_window, textvariable=new_password_var, font=("Arial", 12), width=30, show="*").pack(pady=5)

    tk.Label(signup_window, text="Confirm Password:", font=("Arial", 14), bg="#ffffff", fg="#333").pack(pady=5)
    confirm_password_var = tk.StringVar()
    tk.Entry(signup_window, textvariable=confirm_password_var, font=("Arial", 12), width=30, show="*").pack(pady=5)

    tk.Button(signup_window, text="Register", font=("Arial", 14), bg="#4CAF50", fg="white", width=15, command=register_user).pack(pady=20)

# Function to handle forgot password
def forgot_password():
    def reset_password():
        email_username = email_username_var.get()
        new_password = reset_password_var.get()
        confirm_password = confirm_reset_password_var.get()

        if email_username == "" or new_password == "" or confirm_password == "":
            messagebox.showerror("Error", "All fields are required", parent=forgot_window)
            return

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match", parent=forgot_window)
            return

        ensure_user_database()

        with open("user_database.txt", "r") as file:
            users = file.readlines()

        updated_users = []
        user_found = False

        for user in users:
            stored_username, stored_password = user.strip().split(",")
            if email_username == stored_username:
                updated_users.append(f"{stored_username},{new_password}\n")
                user_found = True
            else:
                updated_users.append(user)

        if not user_found:
            messagebox.showerror("Error", "Username not found", parent=forgot_window)
            return

        with open("user_database.txt", "w") as file:
            file.writelines(updated_users)

        messagebox.showinfo("Success", "Password reset successfully", parent=forgot_window)
        forgot_window.destroy()

    # Forgot Password Window
    forgot_window = tk.Toplevel(root)
    forgot_window.title("Forgot Password")
    forgot_window.geometry("400x350")
    forgot_window.configure(bg="#ffffff")

    tk.Label(forgot_window, text="Reset Password", font=("Arial", 24, "bold"), bg="#ffffff", fg="#333").pack(pady=20)

    tk.Label(forgot_window, text="Username:", font=("Arial", 14), bg="#ffffff", fg="#333").pack(pady=5)
    email_username_var = tk.StringVar()
    tk.Entry(forgot_window, textvariable=email_username_var, font=("Arial", 12), width=30).pack(pady=5)

    tk.Label(forgot_window, text="New Password:", font=("Arial", 14), bg="#ffffff", fg="#333").pack(pady=5)
    reset_password_var = tk.StringVar()
    tk.Entry(forgot_window, textvariable=reset_password_var, font=("Arial", 12), width=30, show="*").pack(pady=5)

    tk.Label(forgot_window, text="Confirm New Password:", font=("Arial", 14), bg="#ffffff", fg="#333").pack(pady=5)
    confirm_reset_password_var = tk.StringVar()
    tk.Entry(forgot_window, textvariable=confirm_reset_password_var, font=("Arial", 12), width=30, show="*").pack(pady=5)

    tk.Button(forgot_window, text="Reset Password", font=("Arial", 14), bg="#2196F3", fg="white", width=20, command=reset_password).pack(pady=20)

# Main Tkinter window
root = tk.Tk()
root.title("Login Screen")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Variables for login
username_var = tk.StringVar()
password_var = tk.StringVar()

# UI Elements
tk.Label(root, text="Welcome Back!", font=("Arial", 26, "bold"), bg="#f0f0f0", fg="#333").pack(pady=20)

tk.Label(root, text="Username:", font=("Arial", 14), bg="#f0f0f0", fg="#333").pack(pady=5)
tk.Entry(root, textvariable=username_var, font=("Arial", 14), width=35, bd=2, relief="groove").pack(pady=5)

tk.Label(root, text="Password:", font=("Arial", 14), bg="#f0f0f0", fg="#333").pack(pady=5)
tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=35, bd=2, relief="groove", show="*").pack(pady=5)

tk.Button(root, text="Forgot Password?", font=("Arial", 12), bg="#f0f0f0", fg="#007BFF", bd=0, command=forgot_password, cursor="hand2").pack(pady=5)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Login", font=("Arial", 14), bg="#4CAF50", fg="white", width=12, command=login).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Cancel", font=("Arial", 14), bg="#f44336", fg="white", width=12, command=root.destroy).grid(row=0, column=1, padx=10)

tk.Button(root, text="Sign Up", font=("Arial", 14), bg="#2196F3", fg="white", width=15, command=signup).pack(pady=10)

root.mainloop()
