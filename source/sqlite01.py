import sqlite3

try:
    db = sqlite3.connect('prueba.db')
    cursor = db.cursor()
except sqlite3.Error:
    print(sqlite3.Error)
print("Conexion exitosa")
sql_statement = 'insert into prueba values("dos", 2, "2020-01-11") '
cursor.execute(sql_statement)
db.commit()
db.close()

