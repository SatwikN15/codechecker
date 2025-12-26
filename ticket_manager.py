import sqlite3

DB_NAME = "database.db"

def connect():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            issue TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def create_ticket(issue):
    initialize_db()
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tickets (issue, status) VALUES (?, ?)",
        (issue, "OPEN")
    )
    conn.commit()
    conn.close()

def get_tickets():
    initialize_db()
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets")
    data = cur.fetchall()
    conn.close()
    return data
