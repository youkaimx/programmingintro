entrada = input("Introduzca un año")
x = int(entrada)
if x % 100 != 0:
 if x % 4 == 0:
  print("Es año biciesto")
 if x % 4 != 0:
  print("No es biciesto")
if x % 100 == 0:
 print("No es biciesto")