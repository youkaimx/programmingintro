# Examen de Segundo Parcial

## Para cada uno de los siguientes incisos, produzca el programa que se le pide. Cuando termine, envíe su trabajo a rvaldez@gmail.com con el Subject (Tema): Examen de Segundo Parcial de "Su nombre completo"

1. El siguiente fragmento de código debe desplegar "Las cadenas coinciden" pero tiene 1 error de sintaxis. Teclee y corrija el programa. Guarde su trabajo como respuesta01.py (10/100)

```pyhton
secreto = "P@ssw0rd"
if secreto = "P@ssw0rd":
    print("Las cadenas coinciden")
else
    print("Las cadenas no coinciden")
```


2. El siguiente fragmento de código debe revisar si el n1 es mayor, menor o igual que n2, pero tiene 3 errores de sintaxis.  Teclee y corrija el fragmento de código. Guarde su trabajo como respuesta02.py (15/100)

```python
n1 = 200
n2 == int(input("Escriba un número "))
if n1 > n2
    print("Mi numero es mayor")
elif n1 < n2:
    print("Tu numero es mayor")
else:
    print "Son iguales los numeros"
```

3. El siguiente fragmento debe calcular la tabla de multiplicar del número que el usuario elija, pero tiene dos errores lógicos. Teclee y corrija. Guarde su trabajo como respuesta03.py (10/100)

```python
factor = 1
tabla = int(input("Imprimir ¿qué tabla? ))
while factor < 10:
    print("Tabla del ", )
print(tabla, " x " , factor, " = ", tabla*factor)
```

4.  Escriba un programa que calcule la suma y reporte el entrenamiento de un equipo de triatlón: El programa deberá comportarse de la siguiente manera (50/100)

```
Nombre del atleta (escribe terminar para terminar): Fulanito de tal
Escriba a continuación las sesiones de entrenamiento:
Natación:
Kilómetros de sesión 1 (-1 para terminar): 1.5
Kilómetros de sesión 2 (-1 para terminar): 2
Kilometros de sesión 3 (-1 para termina): -1
Carrera
Kilómetros de sesión 1 (-1 para terminar): 5
Kilómetros de sesión 2 (-1 para terminar): 7
Kilometros de sesión 3 (-1 para terminar): 5
Kilometros de sesión 4 (-1 para terminar): -1
Ciclismo
Kilómetros de sesión 1 (-1 para terminar): 45
Kilómetros de sesión 2 (-1 para terminar): 45
Kilometros de sesión 3 (-1 para terminar): -1
Resumen para Fulanito de tal. Natación 3.5 km, carrera: 17 km, ciclismo: 90km

Nombre del atleta (escribe terminar para terminar): Hijo de vecino
Escriba a continuación las sesiones de entrenamiento:
Natación:
Kilómetros de sesión 1 (-1 para terminar): 3
Kilómetros de sesión 2 (-1 para terminar): -1
Carrera
Kilometros de sesión 1 (-1 para terminar): -1
Ciclismo
Kilómetros de sesión 1 (-1 para terminar): 45
Kilómetros de sesión 2 (-1 para terminar): 45
Kilómetros de sesión 3 (-1 para terminar): 120
Kilometros de sesión 4 (-1 para terminar): -1
Resumen para Fulanito de tal. Natación 3 km, carrera: 0 km, ciclismo: 210km

Nombre del atleta (escribe terminar para terminar): terminar
Totales:
2 atletas: natación 6.5 km, carrera 17 km, ciclismo 300km
```
Puntuación: 
- 25 puntos por los ciclos de natación, carrera y ciclismo terminados correctamente, con el cálculo correcto. 8 puntos por cada ciclo (+1 por todos correctos). No se adjudican puntos si el ciclo no termina bien o el cálculo no es correcto
- 10 puntos por el ciclo de los atletas, terminado correctamente
- 10 puntos por el cálculo de los totales de atletas, natación, carrera y ciclismo al final del programa. se adjudican 0 puntos si no termina adecuadamente o si no tiene totales correctos
- 5 puntos por el uso de identificadores o variables con nombres significativos, es decir, nombres relacionados a su uso dentro del programa. 
- El programa se debe guardar como respuesta04.py

5. Escriba un programa que lea tres enteros y utilizando el teorema de pitágoras determine si son los lados de un triángulo rectángulo. Por ejemplo:
```
Primer numero: 3
Segundo numero: 4
Segundo numero: 5
Si son lados de un triangulo rectangulo

Primer numero: 8
Segundo numero: 10
Segundo numero: 6
Si son lados de un triangulo rectangulo

Primer numero: 3
Segundo numero: 2
Tercer numero: 1
No son lados de triangulo rectangulo
```
Grabe su programa como respuesta05.py. 15 puntos en total: 5 por el uso de variables con nombres significativos, 5 por la correcta especificación de las condiciones y 5 por el uso de elif. No se adjudicarán puntos si no se ejecuta el programa.