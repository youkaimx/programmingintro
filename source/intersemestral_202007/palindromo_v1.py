cadena = input("escriba una frase o palabra:")
longitud_cadena = len(cadena)
carácter_actual = 0
while carácter_actual < longitud_cadena:
    print("cadena[",carácter_actual, "] = ", cadena[carácter_actual])
    carácter_actual = carácter_actual + 1
