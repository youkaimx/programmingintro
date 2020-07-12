# Leer del teclado dos numeros enteros o asignarlos a dos variables
# Desplegar en la pantalla si cada número es impar o par
# y si el primero es múltiplo de el segundo
# Por ejemplo, si tengo números 6 y 9
# el programa desplegaría
# 6 es par
# 9 es impar
# 6 no es multiplo de 9
primer_numero = 40
segundo_numero = 19
if primer_numero%2==0:
    print("El numero ", primer_numero, " es par")
else:
    print("El numero ", primer_numero, " es impar")
if segundo_numero%2==0:
    print("El numero ", segundo_numero, " es par")
else:
    print("El numero ", segundo_numero, " es impar")
if primer_numero % segundo_numero == 0:
    print( primer_numero,  " es múltiplo de ", segundo_numero)
else:
    print( primer_numero,  " no es múltiplo de ", segundo_numero)