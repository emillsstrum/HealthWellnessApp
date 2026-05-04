import sqlite3

def get_connection() -> sqlite3.Connection:
    # get SQLite connection object
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    return conn
