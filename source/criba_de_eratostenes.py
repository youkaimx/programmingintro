#Criba de eratóstenes
def inicializarLista(lista, numero_elementos):
    indice = 0
    while indice < numero_elementos:
        lista.append(True)
        indice += 1

def imprimePrimos(lista):
    for i in range(2,len(lista)):
        if(lista[i] == True):
            print(i, end=" ")

criba = []
limite_superior = 101
inicializarLista(criba, limite_superior)
print(criba)
for elemento_actual in range(2,limite_superior):
    print("Revisando los multiplos de ", elemento_actual)
    if(criba[elemento_actual] == True):
        multiplo = 2
        while multiplo*elemento_actual < limite_superior:
            criba[elemento_actual*multiplo] = False
            print("El elemento ", elemento_actual * multiplo, "tiene valor ", criba[elemento_actual*multiplo] )
            multiplo = multiplo + 1
print("Los primos del 2 al ", len(criba), " son ")
imprimePrimos(criba)

