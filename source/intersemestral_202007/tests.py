entrada = input("Escribe algo")
#if(entrada.isnumeric()):
#    print(entrada, " califica como numero ", entrada.isnumeric())
#if(entrada.isalnum()):
#    print(entrada, " califica como alfanumerico ", entrada.isalnum() )
#if(entrada.isdecimal()):
#    print(entrada, " califica como decimal ", entrada.isdecimal() )
#if(entrada.isdigit()):
#    print(entrada, " califica como digito", entrada.isdigit())

try:
    numero = float(entrada)
    print("El número si se podría convertir a flotante ")
    print("Elevado al cuadrado sería ", numero*numero)
except ValueError:
    print(entrada, " no se puede convertir a flotante ")
