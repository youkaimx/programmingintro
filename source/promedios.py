archivo = open("/home/rvaldez/Downloads/calificaciones.csv")
alumnos = 0
suma_promedios = 0
for alumno in archivo:
    datos_alumno = alumno.split(",")
    print("Nombre del alumno: ", datos_alumno[0])
    print("Matrícula: ", datos_alumno[1])
    print("Calificaciones: ", end=" ")
    alumnos = alumnos + 1
    suma_calificaciones = 0
    for calificacion in range(2,9):
        print(datos_alumno[calificacion], end=" ")
        suma_calificaciones = suma_calificaciones + int(datos_alumno[calificacion])
    promedio = suma_calificaciones / 7
    suma_promedios = suma_promedios + promedio
    print("Promedio: %.2f"%promedio)
    print()
print("Promedio del grupo: %.2f"%(suma_promedios/alumnos))
archivo.close()


