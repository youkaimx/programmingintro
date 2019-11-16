
def es_hexadecimal(numero):
    caracteres_validos = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f', '0','1','2','3', '4', '5', '6', '7', '8','9']
    i = 0
    #Loop while not at the end of the string AND the current character is valid
    #This stops at the first non valid character or at the end of the string
    #This uses the short circuiting of boolean expression evaluations to avoid the IndexError exception
    while i<len(numero) and numero[i] in caracteres_validos:
        i = i + 1
    #We reached the end of the string? Then it's a valid hexadecimal
    if i == len(numero):
        return True
    #We did not reach the end of the string? It's invalid
    else:
        return False

mi_numero = "CAFEBABE02"
print("Es hexadecimal ", mi_numero, "? ", es_hexadecimal(mi_numero))
mi_numero = "256"
print("Es hexadecimal ", mi_numero, "? ", es_hexadecimal(mi_numero))
mi_numero = "123456abcdefgAz"
print("Es hexadecimal ", mi_numero, "? ", es_hexadecimal(mi_numero))

