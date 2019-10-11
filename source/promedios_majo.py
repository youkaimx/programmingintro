NOMBRE = 0
INGLES = 1
GEOLOGIA = 2
CALCULO = 3
suma_promedios = 0
file = open("promedios.txt")
for promedios in file:
    data = promedios.split (",")
    print("Nombre del alumno: ", data[0])
    print("Calificaciones: ", end=" ")
    NOMBRE = NOMBRE + 1
    suma_calificaciones = 0
    for calificacion in range (1,4) : 
        print(data[calificacion], end=" ")
        suma_calificaciones = suma_calificaciones + int(data[calificacion])
    promedio = suma_calificaciones / 3
    suma_promedios = suma_promedios + promedio
    print("Promedio: %.2f" %promedio)
    print()
print("Promedio del grupo : %.2f" % (suma_promedios/NOMBRE))
file.close()