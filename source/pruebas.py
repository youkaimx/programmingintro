for i in range(5,101,5):
    print(i, end=".")

# For an in memory database
# db = sqlite3.connect(':memory:')

# If customer.db does not exists, it will create it
# db = sqlite3.connect('customer.db')
# use a docstring to define a table
# cursor = db.cursor()
# cursor.execute("""CREATE TABLE customers (
#           first_name text,
#           last_name text,
#           email text
#  )""")
## DATATYPE can be: NULL, INTEGER, REAL, TEXT, BLOB
# db.commit()
# db.close()

# to insert 
# cursor.execute('insert into customer values ("primo", "apellido", "primo@apellido.com" )')
#
# otros = [ 
#  ('isis', 'fernandez', 'isis@fernandez.com'),
#  ('horus', 'escobedo', 'horus@escobedo.com'),
#  ('anubis', 'egipcio', 'anubis@sun.com')
# ]
# cursor.executemany("insert into customers values (?,?,?)", otros)