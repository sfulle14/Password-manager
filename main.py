"""
Project: Password manager
Author: Steven Fuller
Start date: May 8, 2024
Description: The purpose of this project is to create a password manager using modern security concepts.
This passwords and usernames should be hidden until clicked and linked to a website.
"""

import tkinter as tk
from tkinter import messagebox
import database_connection


class AppController:
    def __init__(self, root):
        self.root = root
        self.frames = {}

        for F in (LoginApp, PasswordManagerApp):
            frame = F(root, self)
            self.frames[F] = frame
            frame.main_frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginApp)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.main_frame.tkraise()

class LoginApp:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Password Manager")
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Add Program label
        self.label = tk.Label(self.main_frame, text="Welcome to Password Manager", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)  # Span across both columns
        
        # Add username label
        self.userLabel = tk.Label(self.main_frame, text="UserName:", font=("Arial", 14))
        self.userLabel.grid(row=1, column=0, sticky=tk.E)  # Align to the right (East)
        
        # Add username input
        self.user = tk.Entry(self.main_frame, width=25)
        self.user.grid(row=1, column=1, pady=10)  # Place next to the label
        
        # Add a button to show password
        self.show_button = tk.Button(self.main_frame, text="Login", command=lambda: controller.show_frame(PasswordManagerApp))
        self.show_button.grid(row=3, column=0, columnspan=2, pady=10)


class PasswordManagerApp:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Password Manager")

        # Create main frame
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.grid()
        
        # Add Program label
        self.label = tk.Label(self.main_frame, text="Login worked!", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)  # Span across both columns

        # Add website label
        self.label = tk.Label(self.main_frame, text="Websites", font=("Arial", 14))
        self.label.grid(row=1, column=0, columnspan=2, pady=10)  # Span across both columns

        self.website_entry = tk.Entry(self.main_frame, width=25)
        self.website_entry.grid(row=2, column=0, columnspan=2, pady=10)

        # Add Username label
        self.label = tk.Label(self.main_frame, text="Username", font=("Arial", 14))
        self.label.grid(row=1, column=2, columnspan=2, pady=10)  # Span across both columns

        self.user_entry = tk.Entry(self.main_frame, width=25)
        self.user_entry.grid(row=2, column=2, columnspan=2, pady=10)

        # Add Password label
        self.label = tk.Label(self.main_frame, text="Password", font=("Arial", 14))
        self.label.grid(row=1, column=4, columnspan=2, pady=10)  # Span across both columns

        self.password_entry = tk.Entry(self.main_frame, width=25, show="*")
        self.password_entry.grid(row=2, column=4, columnspan=2, pady=10)


        def save_password(self):
            website = self.website_entry.get()
            username = self.user_entry.get()
            password = self.password_entry.get()
            database_connection.add_account(website, username, password)
            messagebox.showinfo("Info", "Password saved successfully!")

def main():
    database_connection.setup_database()
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
    
    
    