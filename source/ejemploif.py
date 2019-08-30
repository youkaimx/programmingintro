entrada = input("Escribe un numero entero ")
n = int(entrada)
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0
if n > 0:
  print('Es positivo')
  contador_positivos = contador_positivos + 1
if n < 0:
  print('Es negativo')
  contador_negativos = contador_negativos + 1
if n == 0:
  print('Es cero')
  contador_ceros = contador_ceros + 1

entrada = input("Escribe un numero entero ")
n = int(entrada)
if n > 0:
  print('Es positivo')
  contador_positivos = contador_positivos + 1
if n < 0:
  print('Es negativo')
  contador_negativos = contador_negativos + 1
if n == 0:
  print('Es cero')
  contador_ceros = contador_ceros + 1

entrada = input("Escribe un numero entero ")
n = int(entrada)
if n > 0:
  print('Es positivo')
  contador_positivos = contador_positivos + 1
if n < 0:
  print('Es negativo')
  contador_negativos = contador_negativos + 1
if n == 0:
  print('Es cero')
  contador_ceros = contador_ceros + 1

print('Fueron', contador_positivos, ' positivos')
print('Fueron', contador_negativos, ' negativos')
print('Fueron', contador_ceros, ' ceros')