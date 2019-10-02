# Calculo de Pi hasta n términos de la siguiente serie
#  pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...
términos = int(input("Cauntos términos de la serie? "))
términoActual = 1
sumatoria=0
signo=-1
denominador=3
while términoActual < términos:
    sumatoria = sumatoria + signo*4/denominador
    denominador = denominador + 2
    signo = signo * -1
    términoActual = términoActual + 1
print(4+sumatoria)
