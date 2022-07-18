import sqlite3;

conn = sqlite3.connect('ejercicio14/app.db')
cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM Alumnos WHERE nombre = 'Pablo'")
for row in rows:
   print(row)

cursor.close()
conn.close()