
criba = []
limite_superior = 1000

#Inicializar la criba
indice = 0
while indice < limite_superior:
    criba.append(True)
    indice += 1

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

for i in range(2,len(criba)):
    if(criba[i] == True):
        print(i, end=" ")





