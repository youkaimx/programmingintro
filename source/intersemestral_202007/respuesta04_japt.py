numero_atletas=0
total_natacion=0
total_ciclismo=0
total_carrera=0


nombre_atleta=input("Nombre del atleta (escribe terminar para terminar): ")
while nombre_atleta.lower() != "terminar":
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
    total_natacion=total_natacion + kilometros_natacion
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
    total_carrera=total_carrera + kilometros_carrera
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
    total_ciclismo = total_ciclismo + kilometros_ciclismo
    print("Resumen para" ,nombre_atleta, ":", "Natación:", kilometros_natacion, "km", "Carrera:", kilometros_carrera, "km", "Ciclismo:", kilometros_ciclismo, "km" )
    nombre_atleta=input("Nombre del atleta (escribe terminar para terminar): ")
    numero_atletas = numero_atletas + 1

print("Totales:",numero_atletas, "atletas:","Natación:", total_natacion, "km", "Carrera", total_carrera, "km", "Ciclismo", total_ciclismo, "km")