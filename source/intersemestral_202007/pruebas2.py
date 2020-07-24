#respuesta_usuario = 0
#suma_de_respuestas = 0
#while respuesta_usuario >= 0:
#    respuesta_usuario = int(input("-1 para terminar: "))
#    if respuesta_usuario >0:
#        suma_de_respuestas = suma_de_respuestas + respuesta_usuario
#print("La suma de los numeros fue ", suma_de_respuestas)


nombre_atleta=input("Nombre del atleta (escribe terminar para terminar): ")
while nombre_atleta != "terminar":
    print("Escriba a continuación las sesiones de entrenamiento: ")

    print("Natación")
    kilometros = 0
    kilometros_natacion = 0
    sesiones = 1
    while kilometros >= 0:
        print("Kilómetros de sesión ", sesiones, "(-1 para terminar): ", end="")
        kilometros = float(input())
        if kilometros > 0:
            kilometros_natacion = kilometros_natacion + kilometros
        sesiones = sesiones + 1


    print("Carrera")
    kilometros = 0
    kilometros_carrera = 0
    sesiones = 1
    while kilometros >= 0:
        print("Kilómetros de sesión ", sesiones, "(-1 para terminar): ", end="")
        kilometros = float(input())
        if kilometros > 0:
            kilometros_carrera = kilometros_carrera + kilometros
        sesiones = sesiones + 1

    print("Ciclismo")
    kilometros = 0
    kilometros_ciclismo = 0
    sesiones = 1
    while kilometros >= 0:
        print("Kilómetros de sesión ", sesiones, "(-1 para terminar): ", end="")
        kilometros = float(input())
        if kilometros > 0:
            kilometros_ciclismo = kilometros_ciclismo + kilometros
        sesiones = sesiones + 1


    print("Resumen para" ,nombre_atleta, ":", "Natación:", kilometros_natacion, "km", "Carrera:", kilometros_carrera, "km", "Ciclismo:", kilometros_ciclismo, "km" )
    #
    
    nombre_atleta=input("Nombre del atleta (escribe terminar para terminar): ")
