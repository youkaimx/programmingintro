# Ejemplo de como encontrar primos por fuerza bruta
# Se utiliza break para terminar el while cuando se encuentra
# el primer divisor de un número. Observe por ejemplo el caso de 
# los numeros pares: solo se prueba el divisor 2 y después se 
# "rompe" el ciclo while
numero = 2
limite_superior = 50
while numero <= limite_superior:
    es_primo = True
    divisor = 2
    print(">>> Probando divisor: ", end="")
    while divisor < numero:
        print(divisor, end=" ")
        if numero % divisor == 0:
            es_primo = False
            break
        divisor = divisor + 1
    print()
    if es_primo == False:
        print(numero, "no es primo")
    else:
        print(numero, "es primo")
    numero = numero + 1