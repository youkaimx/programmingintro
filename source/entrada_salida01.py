# Este programa muestra el uso de la función input para leer datos del teclado
nombre = input('¿Cómo te llamas?')
print("El usuario dice que se llama ",nombre, " tú ¿le crees?")
numero = input("¿Cuantos años tienes?: ")
# input devuelve lo tecleado como una cadena
# Si queremos interpretarlo como número, debemos convertirlo. La función int
# intenta convertir a entero el argumento que se le da
en4años = int(numero) + 4
# print() espera una cadena. El operador + concatena cadenas
# str convierte su argumento a cadena
print("Al terminar tu carrera vas a tener "+str(en4años)+ " años")