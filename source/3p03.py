def recorrer_caracter(c, desplazamiento):
    letras = "abcdedfghijklmnñopqrstuvwxyz";
    posicion = letras.find(c);
    if posicion>=0:
        return letras[(posicion+desplazamiento)%len(letras)]
    else:
        return c 

frase = "alea iacta est"
print(frase, "con encriptamiento de cesar de 7 posiciones es: ")
for f in frase:
    print(f, " = " , recorrer_caracter(f,7))
