import sqlite3
db = sqlite3.connect("test.db")
cursor = db.cursor()
consulta = "select * from rocasyminerales"
data = cursor.execute(consulta)
print(data)