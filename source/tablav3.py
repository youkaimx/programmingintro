# Este programa despliega la tabla de multiplicar
# del número que el usuario elija
tecleado = input("Tabla de que número quieres que imprima?")
n = int(tecleado)
factor = 1
while factor <= 10   :
    print(factor*n)
    factor = factor + 1
