import sqlite3
db_path = "geologia.db"
database = sqlite3.connect(db_path) 
cursor = database.cursor()
data = ('esmeralda', 'Be3Al2(SiO3)6', 'Es una piedra preciosa muy valorada. Ya en la antigüedad las piedras de color verde, como la malaquita, y la variscita fueron muy apreciadas. La esmeralda une a su color verde especialmente intenso la propiedad de ser transparente o al menos traslúcida, y su mayor brillo al ser pulida. Su nombre, posiblemente persa, significa piedra verde y su tonalidad ha dado nombre al color verde esmeralda')
sql_statement = "insert into piedraspreciosas(nombre,composicion,descripcion) values (?,?,?)"
cursor.execute(sql_statement, data)
database.commit()
database.close()
