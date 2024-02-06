#Contador de números pares(???)
#Por Daniels :D

import os
os.system("cls")

print("CONTADOR DE NÚMEROS PARES")
contpar = 0
cont = 1
n = int(input("\nQuantos números serão inseridos: "))
print()
while cont <= n:
    num = int(input("Número: "))
    if num % 2 == 0:
        contpar += 1
    cont += 1
print("\n", contpar, "números digitados são pares.")