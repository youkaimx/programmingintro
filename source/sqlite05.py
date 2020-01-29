import sqlite3
db_path = "geologia.db"
database = sqlite3.connect(db_path) 
cursor = database.cursor()
data = ('cuarzo rosa', '4')
sql_statement = "update piedraspreciosas set nombre=? where id=?"
cursor.execute(sql_statement, data)
database.commit()
database.close()