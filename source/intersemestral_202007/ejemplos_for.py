# Ejemplos de for
#for v in range(10):
#    print(v

#for i in range(5):
#    print("Hola")

#n! = n * n-1 * n-2 * ... * 1
# n!= 1 * 2 ... * n-1 * n
#n = 5
#factorial = 1
#for f in range(1,n+1):
#    print("Multiplicando por ", f)
#    factorial = factorial * f
#print("Factorial de ", n ," es ", factorial)

# n = 6
# factorial = 1
# for f in range(n,0,-1):
#     print("multiplicando por ", f)
#     factorial = factorial * f
# print("Factorial de ", n, " es ", factorial)


#print("for número in range(10)")
#for número in range(10):
#    print(número, end=" ")
#print()
#print("for número in range(10,20)")
#for número in range(10,20):
#    print(número, end=" ")
#print()
#print("for número in range(20,100, 5)")
#for número in range(20,100, 5):
#    print(número, end=" ")



#CUANTOS=3
#for contador in range(1,CUANTOS+1):
#    número = -1
#    while número <= 0:
#        número = int(input("Escriba un entero positivo:"))
#    print("Entero ", contador, " es ", número)

# 5 x 5
# 5 + 5 + 5 + 5 + 5 = 25
# 2 x 4 = 2 + 2 + 2 + 2 = 8
print("Simular multiplicacion con sumas")
primer_factor = int(input("Escriba el primer factor: "))
segundo_factor = int(input("Escriba el segundo factor: "))
print("Se va a multiplicar", primer_factor, " x ", segundo_factor)
resultado = 0
for i in range(segundo_factor):
    resultado = resultado + primer_factor
print(primer_factor, " x ", segundo_factor, " = ", resultado) 