letras_validas = ["A", "B", "C", "D","E","F"]
numeros_validos = ["0", "1", "2", "3","4","5", "6", "7", "8","9"]
c = input("Escribe un hexadecimal")
es_hexadecimal = True
for cadena in c:
    if cadena.isalpha():
        print(cadena,"es una letra")
        if cadena.upper() in letras_validas:
            print(cadena,"es una letra valida")
        else:
            print("la letra no es valida")
            es_hexadecimal = False
    if cadena.isdecimal():
        print(cadena,"es un numero")
        if cadena in numeros_validos:
            print(cadena,"es un numero valido")
        else:
            print("el numero no es valido")
            es_hexadecimal = False
if es_hexadecimal == True:
    print("la cadena es hexadecimal")
else:
    print("no es hexadecimal")



