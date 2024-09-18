import sqlite3

# Create or connect to a database
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
''')

# Commit and close the connection
conn.commit()
conn.close()
