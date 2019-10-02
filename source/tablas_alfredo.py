#Tabla
tabla_inicial = int(input("Escriba la tabla con la que quiera iniciar: "))
tabla_final = int(input("Escriba la tabla con la que desea terminar: "))
máximo = int(input("Escriba el valor hasta el que desea que se multiplique: "))
for tabla in range(tabla_inicial, tabla_final + 1, 1):
    while tabla_inicial <= tabla_final:
        contador = 1
        while contador < máximo + 1:
                resultado = contador*tabla_inicial
                print(tabla_inicial, "x", contador, "=", resultado, end="    ")
                contador += 1
        print()
        tabla_inicial += 1