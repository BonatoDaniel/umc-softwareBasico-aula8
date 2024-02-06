#Média aritmética de 10 alunos e média aritmética geral
#Por Daniels :D

import os
os.system("cls")

print("MÁDIA DE 10 ALUNOS E MÉDIA GERAL")
mt = 0
for cont in range(1, 11):
    n1 = float(input("\n1ª nota: "))
    n2 = float(input("2ª nota: "))
    m = (n1 + n2) / 2
    print("Média do aluno:", m)
    mt += m
mg = mt / 10
print("\nA média aritmética de todas as médias será", mg)