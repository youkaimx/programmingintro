#NOMBRE=0
#ALTURA=1
#PESO=2
file = open("/home/rvaldez/Nextcloud/Profesional/ITPE/programmingintro/source/alumnos_pesos_alturas.txt")
for linea in file:
    data = linea.split(",")
    #imc = int(data[PESO])/(float(data[ALTURA])**2)  
    imc = int(data[2])/(float(data[1])**2)  
    if imc<20:
        diagnostico = "Bajo de peso"
    elif imc >=20 and imc <=24.9:
        diagnostico = "Peso normal"
    elif imc>=25 and imc<=29.9:
        diagnostico = "Sobrepeso"
    else:
        diagnostico = "Obesidad"
    print(data[0], " diagnóstico: ", diagnostico)
file.close()