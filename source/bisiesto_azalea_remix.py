entrada = input("Escribe un año")
year = int(entrada)

esMultiploDe4 = year%4 == 0
esMultiploDe100 = year%100 == 0

if esMultiploDe4:
    if esMultiploDe100:
        print ("El año no es bisiesto")
    if not esMultiploDe100:
        print("El año es bisiesto")
if not esMultiploDe4:
    print("El año no es bisiesto")

