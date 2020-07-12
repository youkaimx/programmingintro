# Leer 3 números enteros del usuario o asignarlos a una variable
# Determinar cual es el mayor valor de todos
# 10, 20, 5
# 20 es el mayor de todos
primero = 20
segundo = 10
tercero = 2
mayor = primero
if segundo > mayor:
    mayor = segundo
if tercero > mayor:
    mayor = tercero
print("De {} {} {} el valor mayor es {}".format(primero,segundo,tercero, mayor))