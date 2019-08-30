print("Dame un numero entero positivo")
print("cero o negativo para terminar")
entrada = input()
n = int(entrada)
while n > 0:
    if(n%2 == 0):
        print("Es par")
    if(n%2 == 1):
        print("Es impar")
    entrada = input("numero: ")
    n = int(entrada)