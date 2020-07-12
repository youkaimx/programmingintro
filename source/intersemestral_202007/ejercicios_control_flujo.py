# Ejercicios de programación para el tema de control de flujo

# 1. Usando while, escriba un programa que despliegue 
# en 10 líneas, con los números del 10 al 1
numeros=10
while numeros>=1:
    print(numeros)
    numeros = numeros - 1



# Contar de dos en dos, los siguientes códigos son equivalentes
# numeros=10
# while numeros>=1:
#     if numeros%2 == 0:
#         print(numeros)
#     numeros = numeros - 1
# 
# numeros=10
# while numeros>=1:
#     print(numeros)
#     numeros = numeros - 2

# Reescriba el programa de arriba usando for
print("Resultado del ejercicio 2")
valor_inicial = 10
valor_final = 0
variacion = -1
for i in range(valor_inicial,valor_final, variacion):
    print(i)

# Escriba un programa que pregunte por un rango de números e imprima las tablas de 
# multiplicar para ese rango. Por ejemplo
# Empezar con la tabla del: 20
# Terminar con la tabla del: 30
# Nota: Debe asegurarse que el límite superior sea mayor que el límite inferior
# 20      40      60      80      100     120     140     160     180     200
# 21      42      63      84      105     126     147     168     189     210
# 22      44      66      88      110     132     154     176     198     220
# 23      46      69      92      115     138     161     184     207     230
# 24      48      72      96      120     144     168     192     216     240
# 25      50      75      100     125     150     175     200     225     250
# 26      52      78      104     130     156     182     208     234     260
# 27      54      81      108     135     162     189     216     243     270
# 28      56      84      112     140     168     196     224     252     280
# 29      58      87      116     145     174     203     232     261     290
# 30      60      90      120     150     180     210     240     270     300

print("Resultado del ejercicio 3")
limite_inferior = int(input("Tabla a empezar? "))
limite_superior = int(input("Tabla a terminar? "))
while limite_superior <= limite_inferior:
    print("La tabla con la que termine debe ser mayor que ", limite_inferior)
    limite_superior = int(input("Tabla a terminar? "))
tabla_actual = limite_inferior
while tabla_actual <= limite_superior:
    contador = 1
    while contador <= 10:
        resultados = contador * tabla_actual
        print(resultados, end="\t")
        contador = contador + 1
    print()
    # Pasar a la siguiente tabla 
    tabla_actual = tabla_actual + 1