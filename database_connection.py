import sqlite3

def create_connection():
    conn = sqlite3.connect('password_manager.db')  # This will create the database file if it doesn't exist
    return conn

def setup_database():
    conn = create_connection()
    c = conn.cursor()
    # Create accounts table
    c.execute('''CREATE TABLE IF NOT EXISTS accounts
                 (id INTEGER PRIMARY KEY, website TEXT, username TEXT, password TEXT)''')
    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def add_account(website, username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO accounts (website, username, password) VALUES (?, ?, ?)", (website, username, password))
    conn.commit()
    conn.close()

def add_users(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES(?, ?)", (username, password))
    conn.commit()
    conn.close()