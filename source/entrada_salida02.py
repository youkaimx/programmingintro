# Ejemplifica el uso de print para desplegar datos
# e input para leer datos
print("print() puede tomar como argumento una cadena encerrada")
print("\"entre comillas\"")
# end="" indica a print que no añada CR (retorno de carro) y LF (alimentación de línea)
# a la salida, con lo que el siguiente mensaje se imprime en la misma línea del último
# caracter del actual mensaje
nombre = input("¿cómo te llamas? ")
print("hola",nombre,end="")
print(" ¿cómo estás?")
input("Oprima enter para continuar...")