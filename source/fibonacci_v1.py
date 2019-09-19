# Imprime n elementos de la serie de fibonacci

entrada = input("Cuantos elementos? ")
elementos = int(entrada)
n1 = 1
n2 = 1

if elementos >= 1:
    print(n1)
if elementos >= 2:
    print(n2)
if elementos >= 3:
    contador = 2
    while contador < elementos:
        siguiente = n1 + n2
        print(siguiente)
        n1 = n2
        n2 = siguiente
        contador = contador + 1
