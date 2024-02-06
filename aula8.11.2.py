#Mostrar números de 1 a 100 não múltiplos de 3
#Por Daniels :D

import os
os.system("cls")

print("MOSTRAR NÚMEROS DE 1 A 100 NÃO MÚLTIPLOS DE 3\n")
cont = 1
while cont <= 100:
    if cont % 3 != 0:
        print(cont)
    cont += 1