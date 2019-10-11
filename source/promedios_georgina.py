file=open("prom.txt")
numero_de_alumnos = 0;
for alumno in file:
    data = alumno.split(",")
    prom = 0
    suma_promedio=0
    numero_de_alumnos = numero_de_alumnos + 1;
    print("Este es el alumno ", numero_de_alumnos, ", llamado ", data[0])
    for x in range(2,6):
        print("Sumando ", data[x], " a las calificaciones")
        prom = prom + (int(data[x]))
    prom = prom / 4
    suma_promedio = suma_promedio + prom
    print(prom)
file.close