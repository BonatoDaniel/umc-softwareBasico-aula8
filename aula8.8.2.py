#Cálculo da Média aritmética dos N números lidos
#Por Daniels :D

import os
os.system("cls")

print("CÁLCULO DE MÉDIA ARITMÉTICA DE N NÚMEROS LIDOS")
n = int(input("\nValor de N: "))
print()
s = 0
cont = 1
while cont <= n:
    num = float(input("Número: "))
    s += num
    cont += 1
ma = s / n
print("\nA média será", ma)