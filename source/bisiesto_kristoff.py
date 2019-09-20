a=input("ingrese año")   
A=int(a)
if A%4==0 and not A%100==0:
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")
