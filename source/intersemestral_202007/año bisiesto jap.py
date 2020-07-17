print("Este programa lee el año ingresado y checa si es bisiesto o no")
year = input("Por favor, introduzca el año a analizar:")
year = int(year)
if year%400==0:
    print("El año es bisiesto")
# Como no usa else, hay  que revisar por la opción de que NO sea multiplo de 400
if year%4==0 and year%100!=0:
#if year%400!=0 or (year%4==0 and year%100!=0):
    print("El año si es bisiesto") 
if (year%4!=0 and year%100==0) and year%400!=0:
    print("El año no es bisiesto")
# Ya se cubrieron los casos 
#else:
#    print("El año no es bisiesto")
