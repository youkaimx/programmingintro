# Este programa despliega la tabla de multiplicar
# del número que el usuario elija
respuesta = "si"
while respuesta == "si":
    tecleado = input("Tabla de que número quieres que imprima?")
    n = int(tecleado)
    factor = 1
    while factor <= 10   :
        print(factor*n)
        factor = factor + 1
    respuesta = input("Quieres seguir? si o no")
