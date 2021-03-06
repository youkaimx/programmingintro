import string 

def reverse(cadena):
    nueva = ""
    for i in range(len(cadena)-1, -1, -1):
        nueva = nueva + cadena[i]
    return nueva

def deleteSpaces(cadena):
    nueva = ""
    for i in range(0, len(cadena)):
        if cadena[i] not in string.punctuation and not cadena[i].isspace():
            nueva = nueva + cadena[i]
    return nueva

def isPalindrome(cadena):
 revertida = reverse(cadena)
    revertida = deleteSpaces(revertida)
    cadena = deleteSpaces(cadena)
    if cadena.lower() == revertida.lower():
        return True
    else:
        return False
        
print(isPalindrome("ana"))
print(isPalindrome("anitalavalatina"))
print(isPalindrome("miguel"))
print(deleteSpaces("Anita .lava + la       tina?!"))