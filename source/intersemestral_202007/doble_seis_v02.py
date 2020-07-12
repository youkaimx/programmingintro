import random
primera_tirada = random.randint(1,6)
segunda_tirada = random.randint(1,6)
if primera_tirada == segunda_tirada:
    print("Las dos tiradas te dieron el mismo número")
if primera_tirada != segunda_tirada:
    print("Las dos tiradas te dieron números distintos")
print("Este programa ya se acabó")
