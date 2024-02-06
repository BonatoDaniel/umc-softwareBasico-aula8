#Cálculo da Média aritmética dos N números lidos
#Por Daniels :D

import os
os.system("cls")

print("CÁLCULO DE MÉDIA ARITMÉTICA DE N NÚMEROS LIDOS")
n = int(input("\nValor de N: "))
print()
s = 0
for cont in range(1, n+1):
    num = float(input("Número: "))
    s += num
ma = s / n
print("\nA média será", ma)