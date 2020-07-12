# Calculo de Pi hasta n términos de la siguiente serie
#  pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...
términos = int(input("Cuantos términos de la serie? "))
términoActual = 1
pi=0
signo=1
denominador=1
while términoActual <= términos:
    término =  signo*4/denominador
    signo_para_imprimir = "" if signo > 0 else "-"
    print("Añadiendo:", signo_para_imprimir, " 4/",denominador )
    pi = pi +  término
    denominador = denominador + 2
    signo = signo * -1
    términoActual = términoActual + 1
print("El calor de pi calculado por sumatoria de ", términos, " términos es ", pi)
