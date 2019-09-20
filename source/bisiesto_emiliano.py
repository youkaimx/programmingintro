año = int(input('Introduce un año: '))

if año % 4 == 0:
    if año % 100 == 0:
            print('El año no es bisiesto')
    else:
        print('El año es bisiesto.')
else:
    print('El año no es bisiesto.')