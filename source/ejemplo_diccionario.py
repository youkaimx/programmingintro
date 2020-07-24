alumno = {
    "nombre": "Carolina",
    "apellido paterno": "Argudin",
    "apellido materno": "Baqueiro",
    "carrera": "Ingenieria Electrica y Energia",
    "semestre": 3,
    "Programacion": 100,
    "Matematicas 2": 95
}

print(alumno)
print(alumno.keys())
for llave in alumno.keys():
    print(llave, end = " ")
    print(alumno[llave])
