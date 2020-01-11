import sqlite3
db_path = "/Users/rvaldez/Programming/python/programmingintro/source/geologia.db"
database = sqlite3.connect(db_path) 
cursor = database.cursor()
sql_statement = "select * from piedraspreciosas"
data = cursor.execute(sql_statement)
for row in data:
    print("ID: ",row[3], "Nombre: ", row[0], "Composicion: ", row[1])
    print("Descripcion: ", row[2])

database.close()
