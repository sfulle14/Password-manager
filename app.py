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
        
        # Button to login
        self.show_button = tk.Button(self.main_frame, text="Login", command=self.verify_user)
        self.show_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Button to add user
        self.show_button = tk.Button(self.main_frame, text="Add User", command=lambda: controller.show_frame(AddUserApp))
        self.show_button.grid(row=3, column=2, columnspan=1, pady=10)

    def verify_user(self):
        user_list = database_connection.get_user()
        username = self.user.get()
        password = self.password.get()
        for index, row in enumerate(user_list):
            if row[1] == username and row[2] == password:
                self.controller.set_user_id(row[0])
                self.controller.show_frame(PasswordManagerApp)
                self.controller.frames[PasswordManagerApp].show_records(self.controller)
                # self.user_id = row[0]
                return 
        messagebox.showerror("Error", "Wrong Username or Password.")
        

"""
This will congrol the layout of the displayed websites, usernames, and passwords.
"""
class PasswordManagerApp:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Password Manager")
        self.password_labels = {}
        self.index_labels = {}

        # Create main frame
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.grid()

        self.show_records(controller)

    # Function to recreate the display each time it is loaded
    def show_records(self, controller):
        # Delete the widget before being readded
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Add Program label
        self.label = tk.Label(self.main_frame, text="Your Passwords", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)  # Span across both columns

        # Add password Button
        self.add_password_button = tk.Button(self.main_frame, text="Add Password", command=lambda: controller.show_frame(AddPasswordApp))
        self.add_password_button.grid(row=0, column=2)  # Placed at the top right

        # Logout Button
        self.logout_button = tk.Button(self.main_frame, text="Logout", command=lambda: controller.show_frame(LoginApp))
        self.logout_button.grid(row=0, column=4, columnspan=2, sticky=tk.E)  # Placed at the top right

        # labels for the data
        self.label = tk.Label(self.main_frame, text="Websites", font=("Arial", 14))
        self.label.grid(row=1, column=1, columnspan=3, pady=10, sticky=tk.W) 
        self.label = tk.Label(self.main_frame, text="Username", font=("Arial", 14))
        self.label.grid(row=1, column=4, columnspan=3, pady=10, sticky=tk.W)  
        self.label = tk.Label(self.main_frame, text="Password", font=("Arial", 14))
        self.label.grid(row=1, column=7, columnspan=3, pady=10, sticky=tk.W)

        # Loop through records and display them
        records = database_connection.get_records()
        for index, row in enumerate(records):
            # row number and index in database
            index_label = tk.Label(self.main_frame, text=index+1, font=("Arial", 14))
            index_label.grid(row=index+2, column=0, columnspan=1, sticky=tk.W)  # row
            self.index_labels[index] = (index_label, row[0])

            tk.Label(self.main_frame, text=row[1], font=("Arial", 14)).grid(row=index+2, column=1, columnspan=2, sticky=tk.W)  # website
            tk.Label(self.main_frame, text=row[2], font=("Arial", 14)).grid(row=index+2, column=4, columnspan=2, sticky=tk.W)  # username

            # Password
            password_label = tk.Label(self.main_frame, text="*"*10, font=("Arial", 14))
            password_label.grid(row=index+2, column=7, columnspan=2, sticky=tk.W) 
            self.password_labels[index] = (password_label, row[3])
            
            # Show/hide password button
            self.show_password_button = tk.Button(self.main_frame, text="show password", command=lambda idx=index: self.toggle_password_display(idx))
            self.show_password_button.grid(row=index+2, column=9, columnspan=2, sticky=tk.W) 

            # Delete record button
            self.delete_button = tk.Button(self.main_frame, text="delete", command=lambda idx=index: self.delete_record(idx, controller))
            self.delete_button.grid(row=index+2, column=11, columnspan=2, sticky=tk.W) 

    # Function that is called with the delete button is pressed
    def delete_record(self, index, controller):
        label, id = self.index_labels[index]
        database_connection.delete_row(id)
        messagebox.showinfo("Info", "Password deleted successfully!")
        self.controller.show_frame(PasswordManagerApp)
        self.controller.frames[PasswordManagerApp].show_records(controller)

    # Function that toggles the display of password
    def toggle_password_display(self, index):
        label, actual_password = self.password_labels[index]
        current_text = label.cget("text")
        if current_text == "*"*10:
            label.config(text=actual_password)
        else:
            label.config(text="*"*10)
        

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

    # Function that is called when the submit button is pressed
    # This function save the entry into the accounts table
    def save_password(self):
            try:
                website = self.website_entry.get()
                username = self.user_entry.get()
                password = self.password_entry.get()
                user_id = self.controller.get_user_id()
                database_connection.add_account(website, username, password, user_id)
                messagebox.showinfo("Info", "Password saved successfully!")
                self.website_entry.delete(0, tk.END)
                self.user_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.controller.show_frame(PasswordManagerApp)
                self.controller.frames[PasswordManagerApp].show_records(self.controller)
            except:
                messagebox.showerror("Error", "Failed to save password.\n Website already added.")
                self.website_entry.delete(0, tk.END)
                self.user_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.controller.show_frame(AddPasswordApp)
                self.controller.frames[AddPasswordApp]


"""
This app will allow users to create an account
"""
class AddUserApp:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Password Manager")

        # Create main frame
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Add Program label
        self.label = tk.Label(self.main_frame, text="Add new User", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)  # Span across both columns

        # Logout Button
        self.logout_button = tk.Button(self.main_frame, text="Back", command=lambda: controller.show_frame(LoginApp))
        self.logout_button.grid(row=0, column=4, columnspan=2, sticky=tk.E)  # Placed at the top right

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

        # Button to submit new user
        self.show_button = tk.Button(self.main_frame, text="Submit", command=self.save_user)
        self.show_button.grid(row=3, column=0, columnspan=2, pady=10)

    def save_user(self):
        try:
            username = self.user.get()
            password = self.password.get()
            database_connection.add_users(username, password)
            messagebox.showinfo("Info", "User added successfully!")
            self.controller.show_frame(LoginApp)
        except:
            messagebox.showerror("Error", "User already exsits.")


