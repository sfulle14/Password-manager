import sqlite3

# Create the database file
def create_connection():
    conn = sqlite3.connect('password_manager.db')  # This will create the database file if it doesn't exist
    return conn

# Setup the database by creating the tables
def setup_database():
    conn = create_connection()
    c = conn.cursor()
    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    # Create accounts table
    c.execute('''CREATE TABLE IF NOT EXISTS accounts
                 (id INTEGER PRIMARY KEY, website TEXT UNIQUE, username TEXT, password TEXT, userID Integer, FOREIGN KEY(userID) REFERENCES users(id))''')
    conn.commit()
    conn.close()

# Add data to accounts table
def add_account(website, username, password, userID):
    conn = create_connection()
    # c = conn.cursor()
    try:
        with conn:
            conn.execute("INSERT INTO accounts (website, username, password, userID) VALUES (?, ?, ?, ?)", (website, username, password, userID))
    finally:
        conn.close()


# Add data to users table
def add_users(username, password):
    conn = create_connection()
    try:
        with conn:
            conn.execute("INSERT INTO users (username, password) VALUES(?, ?)", (username, password))
    finally:
        conn.close()

# Get count of records in accounts table
def get_record_count():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM accounts")
    count = c.fetchone()[0]
    conn.commit()
    conn.close()
    return count

# Get records from accounts table
def get_records(userId):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM accounts WHERE userID = ?", (userId,))
    records = c.fetchall()
    conn.commit()
    conn.close()
    return records

# Remove a record
def delete_row(idx):
    conn = create_connection()
    try:
        with conn:
            conn.execute("DELETE FROM accounts WHERE id = ?", (idx,))
    finally:
        conn.close()
    
def get_user():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    user_list = c.fetchall()
    conn.commit()
    conn.close()
    return user_list

