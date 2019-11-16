def eshexadecimal(valor):
    letras= ["a","b","c","d","e","f"]
    es_hexadecimal = True
    for x in range(0,len(valor)):
        # print("Ahora estamos revisando el caracter: ", valor[x])
        # print("Estamos en el sector alfabetico")
        if valor[x] not in letras:
            if not valor[x].isdigit():
                # print("Se encontró un digito no valido")
                es_hexadecimal = False
                break
    return es_hexadecimal

entrada = input("inserte valor hexadecimal: ")
resultado = eshexadecimal(entrada.lower())
if resultado == True:
  print(entrada, " es un numero hexadecimal valido")
else:
  print(entrada, " no es un numero hexadecimal valido")