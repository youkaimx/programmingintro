#!env python3
print("Cálculo de una base elevada a una potencia")
data = input("Escriba un número entero para la base: ")
base = int(data)
data = input("Escriba un número entero para la potencia: ")
potencia = int(data)
contador = 1
resultado = base
while contador < potencia:
    resultado = resultado * base
    contador = contador + 1
print(str(base) + " elevado a la potencia " + str(potencia) + " es igual a: " + str(resultado))