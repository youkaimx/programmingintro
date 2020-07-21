#factor = 1
#tabla = int(input("Imprimir ¿qué tabla?" ))
#while factor < 10:
#    print("Tabla del ", )
#print(tabla, " x " , factor, " = ", tabla*factor)

#Carolina 
#factor = 1
#tabla = int(input("Imprimir ¿qué tabla?"))
#while factor <= 10:
#    print(tabla, " x " , factor, " = ", tabla*factor)
#    factor=factor+1



# JA Peon
#factor=1
#tabla=int(input("Imprimir ¿qué tabla?"))
#while factor <= 10:
#    print(tabla, " x " , factor, " = ", tabla*factor)
#    factor=factor + 1


n1=input("ingrese un numero entero")
n2=input("ingrese un numero entero")
n3=input("ingrese un numero entero")
n1=int(n1)
n2=int(n2)
n3=int(n3)
if n1**2+n2**2==n3**2:
     print("es triangulo rectangulo, n3 es su hipotenusa")
elif n2**2+n3**2==n1**2:
     print("es triangulo rectangulo, n1 es su hipotenusa")
elif n3**2+n1**2==n2**2:
     print("es triangulo rectangulo, n2 es su hipotenusa")
else:
     print("no es triangulo rectangulo")