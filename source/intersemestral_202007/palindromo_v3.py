cadena = input("escriba una frase o palabra:")
longitud_cadena = len(cadena)
carácter_actual = 0
while carácter_actual < longitud_cadena:
    print(cadena[carácter_actual], end=" ")
    carácter_actual = carácter_actual + 1
print()
carácter_actual =  longitud_cadena - 1
while carácter_actual >= 0:
    print(cadena[carácter_actual], end=" ")
    carácter_actual = carácter_actual - 1

# cadena = input("escriba una frase o palabra:")
# cadena2 = cadena.replace(" ", "")
# print(cadena2)
