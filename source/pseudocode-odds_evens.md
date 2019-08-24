```
LEER veces
contador <- 0
pares <- 0
impares <- 0
MIENTRAS(contador < veces)
   LEER numero
   SI(numero % 2 = 0)
   ENTONCES
      pares <- pares + 1
   FIN DE SI 
   SI(numero % 2 <> 0)
   ENTONCES
     impares <- impares + 1
   FIN DE SI
   contador <- contador + 1
FIN DE MIENTRAS
DESPLEGAR pares, impares
```
