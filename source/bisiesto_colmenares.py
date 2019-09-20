print ("indique que año desea saber si es bisiesto")
año = input()
año = int(año)
if año % 100 != 0 and año % 4 == 0:
    print (año, "es bisiesto")
else:
    print (año, "no es bisiesto")