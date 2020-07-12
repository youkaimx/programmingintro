#factor = 1
#while factor <= 100:
#    print(factor, end=" ")

#respuesta_usuario = "si"
#while respuesta_usuario == "si":
#    print("Aqui deberia hacer algo")
#    respuesta_usuario = input("Quieres seguir haciendo algo? (si para continuar) ")

import random
dado1=-1
dado2=-1
haTiradoDobleSeis=False
while not haTiradoDobleSeis:
   input("Oprima enter para tirar los dados")
   dado1 = random.randint(1,6)
   dado2 = random.randint(1,6)
   print("Dado 1: ", dado1, ", dado 2: ", dado2)
   haTiradoDobleSeis=dado1==6 and dado2==6
print("Felicidades! Tiraste un doble 6")