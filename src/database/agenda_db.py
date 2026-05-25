import sqlite3

conn = sqlite3.connect(
    "data/agenda.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS agenda (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    data TEXT,
    horario TEXT
)
""")

conn.commit()