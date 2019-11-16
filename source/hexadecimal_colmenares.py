num = ["0","1","2","3","4","5","6","7","8","9"]
let = ["a","b","c","d","e","f"]
print("Cual es el numero que desea saber si es hexadecimal?")
hexa = input()
hexa = hexa.lower()
for x in range (0,len(hexa),1):
    if hexa[x] not in num:
        if hexa [x] not in let:
            print("No es hexadecimal")
            break
        else:
            print("Es hexadecimal")
            break
