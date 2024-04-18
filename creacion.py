import sqlite3 as sql

# Crear database
db = sql.connect('data.db')
cursor = db.cursor()
cursor.execute('''
ALTER TABLE Concentrado
DROP COLUMN id_boutique;
               
               
                            ''')
db.commit()
db.close()
