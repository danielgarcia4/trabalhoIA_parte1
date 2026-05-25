import sqlite3

conn = sqlite3.connect(
    "data/tasks.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarefa TEXT,
    concluida INTEGER DEFAULT 0
)
""")

conn.commit()