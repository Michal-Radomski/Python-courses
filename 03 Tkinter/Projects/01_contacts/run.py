import sqlite3  # *Python's standard library, specifically the Lib/sqlite3/

# Connect to the database (creates 'contacts.db' if it doesn't exist)
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create the table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS contacts_list (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        number INTEGER NOT NULL UNIQUE
    )
"""
)

# Commit changes and close connection
conn.commit()
conn.close()

print("Table 'contacts_list' created successfully!")
