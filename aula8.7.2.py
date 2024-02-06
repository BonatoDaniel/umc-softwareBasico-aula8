#Exibir somatória dos números de 1 a N
#Por Daniels :D

import os
os.system("cls")

print("EXIBIR SOMATÓRIA DOS NÚMEROS DE 1 A N")
n = int(input("\nValor de N: "))
s = 0
cont = 1
while cont <= n:
    s += cont
    cont += 1
print("\nA soma será", s)