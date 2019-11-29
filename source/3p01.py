def mayor_de_la_lista(lista):
    mayor = lista[0]
    for n in range(1,len(lista)):
        if lista[n] > mayor:
            mayor = lista[n]
    return mayor


lista_uno = [ 10, 20, 100, 90, 60, 50, 30, 75, 42, 89 ]
print("El mayor de", lista_uno, " es: ", mayor_de_la_lista(lista_uno));
lista_dos = []
entrada = input("Escriba un numero, cualquier otra cosa para terminar: ")
while entrada.isnumeric():
    lista_dos.append(float(entrada))
    entrada = input("Escriba un numero, cualquier otra cosa para terminar: ")
print("El mayor de", lista_dos, " es: ", mayor_de_la_lista(lista_dos));
