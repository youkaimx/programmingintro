import string
def imprimir_lista(lista):
    for elemento in lista:
        for llave in elemento.keys():
            print(elemento[llave], end=" ")
        print() # Comenzar una nueva linea despues de imprimir el diccionario

lista_super = [
               { "producto": "trix", "cantidad": 3 },
               { "producto": "pan bimbo", "cantidad": 1},
               { "producto": "skippy", "cantidad": 1},
               { "producto": "mermelada de fresa", "cantidad": 1},
               { "producto": "manzanas", "cantidad": 14},
               { "producto": "platanos", "cantidad": 7}
               ]
print("Esta es la lista del super")
imprimir_lista(lista_super)
respuesta = input("Quieres cambiar las cantidades o nombres de algo? ")
if respuesta.lower() == "si":
    for cosa in lista_super:
        print(cosa["producto"])
        nuevacosa = input("Nuevo producto o enter para dejar igual: ")
        if not nuevacosa.isspace() and len(nuevacosa) > 0: 
            cosa["producto"] = nuevacosa
        print(cosa["cantidad"])
        # Evitar que se termine el programa cuando no dan un número
        try:
            nuevacantidad = int(input("Cantidad o -1 para dejar igual: "))
        except ValueError:
            nuevacantidad = -1
        if not nuevacantidad == -1:
            cosa["cantidad"] = nuevacantidad
    print("Esta es la nueva lista")
    imprimir_lista(lista_super)