NOMBRE=0
ALTURA=1
PESO=2
file = open("alumnos_pesos_alturas.txt")
for linea in file:
    data = linea.split(",")
    imc = int(data[PESO])/(float(data[ALTURA])**2)  
    if imc<20:
        diagnostico = "Bajo de peso"
    elif imc >=20 and imc <=24.9:
        diagnostico = "Peso normal"
    elif imc>=25 and imc<=29.9:
        diagnostico = "Sobrepeso"
    else:
        diagnostico = "Obesidad"
    print(data[NOMBRE], " diagnóstico: ", diagnostico)
file.close()