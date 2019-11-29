def formatear_fecha(fecha):
    meses = { 1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 
            7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
    return str(fecha["dia"]) + " de " + meses[fecha["mes"]] + " de " + str(fecha["año"])
f = { "dia": 28, "mes": 11, "año": 2019}
print("Formatear fecha ", formatear_fecha(f) )
f["dia"] = int(input("Dia: "))
f["mes"] = int(input("Mes: "))
f["año"] = int(input("Año: "))
print("Formatear fecha ", formatear_fecha(f) )