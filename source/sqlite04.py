import sqlite3
db_path = "geologia.db"
database = sqlite3.connect(db_path) 
cursor = database.cursor()
sql_statement = "delete from piedraspreciosas where nombre='foo'"
data = cursor.execute(sql_statement)
database.commit()
database.close()