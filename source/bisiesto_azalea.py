entrada = input("Escribe un año")
year = int(entrada)
if year%4 == 0:
    if (year%100) != 0:
        print ("El año es bisiesto")
if year%4 != 0:
    if (year%100) == 0:
        print ("El año no es bisiesto")
