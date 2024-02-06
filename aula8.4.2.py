#Mostrar números ao quadrado
#Por Daniels :D

import os
os.system("cls")

print("NÚMEROS AO QUADRADO")
v = int(input("\nQuantos números serão calculados: "))
x = 1
while x <= v:
    n = int(input("\nNúmero: "))
    r = n ** 2
    print(r)
    x += 1