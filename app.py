"""
The program will hold all the functionality of the application.
"""
import tkinter as tk
from tkinter import messagebox
import database_connection

"""
This will control the login page functionality
"""
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

        # Add password label
        self.passwordLabel = tk.Label(self.main_frame, text="Password:", font=("Arial", 14))
        self.passwordLabel.grid(row=2, column=0, sticky=tk.E)  # Align to the right (East)
        
        # Add password input
        self.password = tk.Entry(self.main_frame, width=25)
        self.password.grid(row=2, column=1, pady=10)  # Place next to the label
        
        # Add a button to show password
        self.show_button = tk.Button(self.main_frame, text="Login", command=lambda: controller.show_frame(PasswordManagerApp))
        self.show_button.grid(row=3, column=0, columnspan=2, pady=10)


"""
This will congrol the layout of the displayed websites, usernames, and passwords.
"""
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

        # Add password Button
        self.add_password_button = tk.Button(self.main_frame, text="Add Password", command=lambda: controller.show_frame(AddPasswordApp))
        self.add_password_button.grid(row=0, column=2)  # Placed at the top right

        # Logout Button
        self.logout_button = tk.Button(self.main_frame, text="Logout", command=lambda: controller.show_frame(LoginApp))
        self.logout_button.grid(row=0, column=3, sticky=tk.E)  # Placed at the top right

        for i in range(database_connection.get_record_count()):
            # Add website label
            self.label = tk.Label(self.main_frame, text="Websites", font=("Arial", 14))
            self.label.grid(row=1, column=0, columnspan=2, pady=10)  # Span across both columns

            # Add Username label
            self.label = tk.Label(self.main_frame, text="Username", font=("Arial", 14))
            self.label.grid(row=1, column=2, columnspan=2, pady=10)  # Span across both columns

            # Add Password label
            self.label = tk.Label(self.main_frame, text="Password", font=("Arial", 14))
            self.label.grid(row=1, column=4, columnspan=2, pady=10)  # Span across both columns


"""
This will control how websites, usernames, and passwords are added.
"""
class AddPasswordApp:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Password Manager")

        # Create main frame
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Add Program label
        self.label = tk.Label(self.main_frame, text="Add Login Data", font=("Arial", 14))
        self.label.grid(row=0, column=2, columnspan=2, pady=10)  # Span across both columns

        # Back button
        self.back_button = tk.Button(self.main_frame, text="Back", command=lambda: controller.show_frame(PasswordManagerApp))
        self.back_button.grid(row=0, column=0, columnspan=2, pady=10) 

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

        self.password_entry = tk.Entry(self.main_frame, width=25)
        self.password_entry.grid(row=2, column=4, columnspan=2, pady=10)

        # Add password Button
        self.add_password_button = tk.Button(self.main_frame, text="Submit", command=self.save_password)
        self.add_password_button.grid(row=3, column=2, columnspan=2, pady=10)  # Placed at the top right

    def save_password(self):
            website = self.website_entry.get()
            username = self.user_entry.get()
            password = self.password_entry.get()
            database_connection.add_account(website, username, password)
            messagebox.showinfo("Info", "Password saved successfully!")
            self.controller.show_frame(PasswordManagerApp)
