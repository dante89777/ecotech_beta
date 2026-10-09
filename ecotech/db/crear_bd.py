import sqlite3

conn = sqlite3.connect("ecotech.db")

conn.executescript(
    open("db/01_esquema.sql", encoding="utf-8").read()
)

conn.close()

print("Base creada correctamente")