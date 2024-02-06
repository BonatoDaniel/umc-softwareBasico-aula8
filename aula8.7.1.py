#Exibir somatória dos números de 1 a N
#Por Daniels :D

import os
os.system("cls")

print("EXIBIR SOMATÓRIA DOS NÚMEROS DE 1 A N")
n = int(input("\nValor de N: "))
s = 0
for cont in range(1, n+1):
    s += cont
print("\nA soma será", s)