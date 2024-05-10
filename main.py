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
from app import LoginApp, PasswordManagerApp, AddPasswordApp, AddUserApp


class AppController:
    def __init__(self, root):
        self.root = root
        self.frames = {}

        for F in (LoginApp, PasswordManagerApp, AddPasswordApp, AddUserApp):
            frame = F(root, self)
            self.frames[F] = frame
            frame.main_frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginApp)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.main_frame.tkraise()
    

def main():
    database_connection.setup_database()
    root = tk.Tk()
    root.geometry("800x600")
    app = AppController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
    
    
    