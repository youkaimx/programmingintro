import random
primera_tirada = random.randint(1,6)
segunda_tirada = random.randint(1,6)
if primera_tirada == segunda_tirada:
    print("d1: ", primera_tirada)
    print("d2: ", segunda_tirada)
    print("Las dos tiradas te dieron el mismo número")
else:
    print("d1: ", primera_tirada, "d2: ", segunda_tirada)
    print("Las dos tiradas te dieron números distintos")
print("Este programa ya se acabó")