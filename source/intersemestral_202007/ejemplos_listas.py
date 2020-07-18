# lista = [ "Carolina", [20, 40, 30 ] , "Jose Antonio", [15, 40, 35 ] ]
# lista.append("Kristoff")
# 
# for alumno in lista:
#     print(alumno)
# 
# l2 = [ 1, 2, 3, 4 ]
# if 3 in l2:
#     print(3, "si está en l2")

alumno=[]
alumnos=[]
hayMasAlumnos = True
while hayMasAlumnos:
    nombre = input('Nombre o enter para terminar: ')
    if len(nombre)==0:
        hayMasAlumnos = False
    else:
        matricula = input('Matricula del alumno ')
        alumnos.append([nombre, matricula])
print("El grupo completo es ")
print(alumnos)