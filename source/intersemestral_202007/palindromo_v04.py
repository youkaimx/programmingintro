cadena = input("escriba una frase o palabra:")
longitud_cadena = len(cadena)

ultimo_carácter = len(cadena) -1
for c in cadena:
    print(c,"=>", cadena[ultimo_carácter])
    ultimo_carácter = ultimo_carácter - 1
