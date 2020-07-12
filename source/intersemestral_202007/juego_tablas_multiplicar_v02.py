# Hacer un juego para practicar las tablas de multiplicar
# El usuario tecleará cuantas preguntas quiere responder y 
# de que tabla de multiplicar. 
# El programa aleatoriamente preguntará por multiplicaciones
# de esa tabla hasta llegar al número que el usuario pidió
# Al final el programa desplegará número de aciertos y número de 
import random
tabla = int(input("Que tabla quieres practicar? "))
cantidad_aciertos = 0
cantidad_fallos = 0
respuesta_usuario = "si"
while respuesta_usuario.upper() == "SI":
    # Preguntar por las tablas
    factor = random.randint(1,10)
    print("Cuanto es ", tabla, " x ", factor, "? ", end=" ")
    respuesta = int(input())
    if respuesta == tabla*factor:
        print("¡Es correcto!")
        cantidad_aciertos = cantidad_aciertos + 1
    else:
        print("Cerca! pero no. ", tabla, " x ", factor,  " = ", tabla*factor)
        cantidad_fallos = cantidad_fallos + 1
    respuesta_usuario = input("Escribe si para continuar. Cualquier otra cosa para terminar: ")

#print("Aciertos: ", cantidad_aciertos)
#print("Fallos: ", cantidad_fallos)
#entrada = input("Escribe algo: ")
#print("En mayusculas", entrada.upper())
#print("En minusculas", entrada.lower())