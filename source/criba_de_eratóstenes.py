#Criba de eratóstenes

def inicializarLista(lista, numero_elementos):
    indice = 0
    while indice < numero_elementos:
        lista.append(True)
        indice += 1


criba = []
inicializarLista(criba, 15)
print(criba)