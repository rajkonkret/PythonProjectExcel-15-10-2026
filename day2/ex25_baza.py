import sqlite3

try:
    conn = sqlite3.connect("baza.db")
    cursor = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS users
               (
                   id
                   INTEGER,
                   name
                   TEXT
               );
            """

    conn.execute(query)
    conn.commit()
except sqlite3.Error as e:
    print("Bład bazy:", e)
finally:
    if conn:
        conn.close()
