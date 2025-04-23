#frontend code
import tkinter as tk
from tkinter import messagebox
import requests

def login():
    email = email_entry.get()
    password = password_entry.get()

    response = requests.post("http://127.0.0.1:5000/login", json={
    
        "email": email,
        "password": password
    })

    if response.status_code == 200:
        messagebox.showinfo("Success", response.json()["message"])
    else:
        messagebox.showerror("Failed", response.json()["message"])

# GUI
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

tk.Label(root, text="Email").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()
