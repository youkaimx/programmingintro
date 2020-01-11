import sqlite3
db_path = "/Users/rvaldez/Programming/python/programmingintro/source/geologia.db"
database = sqlite3.connect(db_path) 
cursor = database.cursor()
sql_statement = "delete from piedraspreciosas where id=3"
data = cursor.execute(sql_statement)
database.commit()
database.close()
