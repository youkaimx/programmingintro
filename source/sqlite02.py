import sqlite3
db_path = "/Users/rvaldez/Programming/python/programmingintro/source/geologia.db"

database = sqlite3.connect(db_path) 
cursor = database.cursor()
data = ('aguamarina', 'Be3Al2Si6O18::Fe', 'El aguamarina es la variedad de color azul verdoso pálido del berilo al igual que la esmeralda. Se trata de una gema muy apreciada en joyería por su dureza, permitiendo una gran diversidad de cortes. Su color y brillo recuerdan al agua del mar.')
sql_statement = "insert into piedraspreciosas(nombre,composicion,descripcion) values (?,?,?)"
cursor.execute(sql_statement, data)
database.commit()
database.close()
