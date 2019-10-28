
import csv
def leer_archivo(nombre, campos):
    lista = []
    archivo_csv = open(nombre, "r")
    lector_csv = csv.DictReader(archivo_csv, fieldnames = campos)
    for linea in lector_csv:
        lista.append(linea)
    archivo_csv.close()
    return lista
    
def imprimir_lista(lista):
    campos = list(lista[0])
    for linea in lista:
        for campo in campos:
            print(campo, ":", end=" ")
            print(linea[campo])

def imprimir_lista_horizontal(lista, imprimir_encabezados=False):
    campos = list(lista[0])
    if(imprimir_encabezados):
        for campo in campos:
            msg = ("%s\t"%campo).expandtabs(12)
            print(msg,end="")
        print()
    for linea in lista:
        for campo in campos:
            msg = ("%s\t"%linea[campo]).expandtabs(12)
            print(msg,end="")
        print()

def calcular_promedio(lista):
    promedios = []
    #list on the dictionary returns a list of keys
    llaves = list(lista[0])
    materias = llaves[1:]
    for linea in lista:
        matricula = linea['matricula']
        promedio_alumno = {'matricula': matricula, 'promedio': 0}
        for materia in materias:
                promedio_alumno['promedio']= promedio_alumno['promedio'] + int(linea[materia])
        promedio_alumno['promedio'] = promedio_alumno['promedio']/len(materias)
        promedios.append(promedio_alumno)
    return promedios


estructura_archivo_calificaciones = [ "matricula", "A", "B", "C", "D" ]
estructura_archivo_alumnos = [ "matricula", "nombres", "apellido paterno", "apellido materno", "programa"]
alumnos = leer_archivo("alumnos.csv", estructura_archivo_alumnos)
primer_parcial = leer_archivo("01parcial.csv", estructura_archivo_calificaciones)
segundo_parcial = leer_archivo("02parcial.csv", estructura_archivo_calificaciones)
imprimir_lista(alumnos)
imprimir_lista_horizontal(primer_parcial,  True)
imprimir_lista(calcular_promedio(primer_parcial))