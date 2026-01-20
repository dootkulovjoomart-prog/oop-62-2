import sqlite3
connect = sqlite3.connect('orders.db')
cursor = connect.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
)""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        total INTEGER,
        user id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
)""")