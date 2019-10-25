def reverse(cadena):
    nueva = ""
    for i in range(len(cadena)-1, -1, -1):
        nueva = nueva + cadena[i]
    return nueva

def deleteSpaces(cadena):
    nueva = ""
    for i in range(0, len(cadena)):
        if cadena[i] != ' ':
            nueva = nueva + cadena[i]
    return nueva

def isPalindrome(cadena):
    revertida = reverse(cadena)
    if cadena == revertida:
        return True
    else:
        return False

print(isPalindrome("ana"))
print(isPalindrome("anitalavalatina"))
print(isPalindrome("miguel"))