def eshexadecimal(numero):
    numeros_validos = ["0","1","2","3","4","5","6","7","8","9"]
    letras_validas = ["A","B","C","D","E","F"]
    resultado = True
    for c in numero:
        #print("Estamos revisando el caracter ", c)
        while resultado == True:
            if c not in numeros_validos and c.upper() not in letras_validas:
               #print("Encontre un caracter invalido")
                resultado = False
                break
            else:
                break
    return resultado

numero = input("Ingrese un número: ")
resultado = eshexadecimal(numero)
if resultado == True:
    print("El número es hexadecimal")
else: 
    print("No es hexadecimal")
