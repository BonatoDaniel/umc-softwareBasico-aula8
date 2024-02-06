#Mostrar números pares entre 1 e X
#Por Daniels :D

import os
os.system("cls")

print("NÚMEROS PARES ENTRE 1 E X")
n = int(input("\nNúmero máximo: "))
print()
x = 2
while x <= n:
    print(x)
    x += 2