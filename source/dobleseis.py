#Tirar dos dados hasta conseguir un doble 6
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