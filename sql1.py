import sqlite3

conn = sqlite3.connect("musica.sqlite")
cur  = conn.cursor()

#cur.execute("DROP TABLE IF EXISTS Canciones")
#cur.execute("CREATE TABLE Canciones (titulo TEXT,reproducciones INTEGER)")

cur.execute("INSERT INTO Canciones (titulo,reproducciones) VALUES (?,?)",("Thunderstruck",20))
cur.execute("INSERT INTO Canciones (titulo,reproducciones) VALUES (?,?)",("My way",15))
conn.commit()

print("Canciones:")
cur.execute("Select titulo, reproducciones FROM Canciones")
for fila in cur:
    print (fila)
cur.execute("DELETE FROM Canciones WHERE reproducciones < 100")
conn.commit()
cur.close()

#conn.close()