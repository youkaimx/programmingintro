tablaInicial = int(10)
tablaFinal = int(20)
print("Tablas del 10 al 20")
while tablaInicial <= tablaFinal:
    factor = 1
    while factor <= 10:
        print(tablaInicial * factor, end="\t")
        factor = factor + 1    
    tablaInicial= tablaInicial + 1
    print()
    