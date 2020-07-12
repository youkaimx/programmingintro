import random

primera_tirada = random.randint(1,6)
segunda_tirada = random.randint(1,6)
son_iguales_las_tiradas = primera_tirada == segunda_tirada
print("El primer tiro de dado te dio " + str(primera_tirada))
print("El segundo tiro fue ", segunda_tirada)
print("Tiraste el mismo número ambas veces? ", son_iguales_las_tiradas)

