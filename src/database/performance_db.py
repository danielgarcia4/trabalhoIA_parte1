import sqlite3

conn = sqlite3.connect(
    "data/performance.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS performance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    score INTEGER
)
""")

conn.commit()

def save_performance(
    topic,
    score
):

    cursor.execute("""
    INSERT INTO performance (
        topic,
        score
    )
    VALUES (?, ?)
    """, (
        topic,
        score
    ))

    conn.commit()