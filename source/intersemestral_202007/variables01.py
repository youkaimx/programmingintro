nombre_alumno = 'Fulanito de tal'
edad_alumno = 19
MAYORIA_DE_EDAD_LEGAL = 18
CALIFICACION_MINIMA = 7.0
promedio = 9.1
es_mayor_de_edad = edad_alumno >= MAYORIA_DE_EDAD_LEGAL
esta_reprobado = promedio < CALIFICACION_MINIMA
print(nombre_alumno)
print('¿Es mayor de edad? ', end="")
print(es_mayor_de_edad)
print('¿Está reprobado? ', end="")
print(esta_reprobado)