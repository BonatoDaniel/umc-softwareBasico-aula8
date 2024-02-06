#Mostrar números ao quadrado
#Por Daniels :D

import os
os.system("cls")

print("NÚMEROS AO QUADRADO")
v = int(input("\nQuantos números serão calculados: "))
for x in range(1, v+1):
    n = int(input("\nNúmero: "))
    r = n ** 2
    print(r)