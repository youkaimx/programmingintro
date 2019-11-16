hexadecimal = input("Escriba un valor hexadecimal: ")
letras_validas = ['a', 'b', 'c', 'd', 'e', 'f']
numeros_valido = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
for letras in hexadecimal:
    if letras.isalpha():
        print(letras, "es una letra")
    if letras.isnumeric():
        print(letras, "es un numero")
    if letras in letras_validas or letras.isnumeric():
        print(letras, "pertenece al sistema")
    else:
        print(letras, "no pertenece al sistema")