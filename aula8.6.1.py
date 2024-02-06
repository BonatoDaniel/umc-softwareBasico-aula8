#Mostrar números pares entre 1 e X
#Por Daniels :D

import os
os.system("cls")

print("NÚMEROS PARES ENTRE 1 E X")
n = int(input("\nNúmero máximo: "))
print()
for x in range(2, n+1, 2):
    print(x)