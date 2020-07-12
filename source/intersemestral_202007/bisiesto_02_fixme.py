#Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100,
# y también si es divisible entre 400.

try:
    año = input("Por favor escribe un año ")
    año = int(año)
    if año % 400 == 0:
        print("Si es bisiesto")
    if año%4 == 0 and año%100 != 0:
        print("si es bisiesto")
    else:
        print("No es bisiesto")
except ValueError:
    print(año, " no es un numero entero")
print("Adios")