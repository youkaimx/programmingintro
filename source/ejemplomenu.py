def insertarDatos():
    # Aqui se copia el codigo para 
    # conectarme a la base de datos, abrir un cursor, leer datos y luego hacer un inser

def leerDatos():

print("Catalogo de piedras preciosas")
respuesta = "1"
while respuesta != 5:
    print("1 Insertar datos")
    print("2 Leer datos")
    print("5. Salir" )
    respuesta = int(input("Que opcion quieres"))
    if respuesta == 1:
        insertarDatos()
    if respuesta == 2:
        leerDatos()
    if respuesta == 5:
        print("Gracias por usar mi sistema de inventario")
    
