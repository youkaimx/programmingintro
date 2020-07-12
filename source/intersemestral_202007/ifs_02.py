# Revisar si la calicacion está entre 100 y 90 - asignar A
# si 89 y 80 asignar B
# si está entre 79 y 70 asignar C
# si está entre 69 y 60 asignar D
# si es menor que 59 asignar F
# Las calificaciones validas están entre 100 y 0
calificación = 85
if calificación <= 100 and calificación >= 0:
    print("Es una calificación válida")
    if calificación <= 100 and calificación >= 90:
        print(calificación, " tiene un valor alfabético de A ")
    if calificación <= 89 and calificación >= 80:
        print(calificación, " tiene un valor alfabético de B ")
    if calificación <= 79 and calificación >= 70:
        print(calificación, " tiene un valor alfabético de C ")
    if calificación <= 69 and calificación >= 60:
        print(calificación, " tiene un valor alfabético de D ")
    if calificación <= 59 and calificación >= 0:
        print(calificación, " tiene un valor alfabético de F ")
else:
    print("Esa no es una calificación válida")