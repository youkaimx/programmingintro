#!/usr/bin/python3
entrada = input("Cuantas lineas: ")
lineas = int(entrada)
# Cuadrados
n = 0
while n < lineas:
  print('*'*lineas)
  n = n + 1
print()
n=1
while n<=lineas:
  print('*'*n)
  n=n+1
print()
n=lineas - 1
while(n>=0):
  print(' '*n,end="")
  print("*"*(lineas-n))
  n=n-1
print()
n=lineas
while n>0:
  print("*"*n)
  n=n-1
print()
  
n=lineas
while n>0:
  print(" "*(lineas - n),end="")
  print("*"*n)
  n=n-1
print()
