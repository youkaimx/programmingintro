cadena = input("escriba una frase o palabra:")
carácter_actual =  len(cadena) - 1 
while carácter_actual >= 0:
    print("cadena[",carácter_actual, "] = ", cadena[carácter_actual])
    carácter_actual = carácter_actual - 1