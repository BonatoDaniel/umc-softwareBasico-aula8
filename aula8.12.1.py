#Calcula a média de cada aluno e apresenta o número de aprovados e reprovados
#Por Daniels :D

import os
os.system("cls")

print("CÁLCULO DE MÉDIA DE 60 ALUNOS E NÚMERO DE APROVADOS E REPROVADOS")
ap = 0
re = 0
ex = 0
for cont in range(1, 61):
    n1 = float(input(f"\n{cont}º aluno\nNota 1: "))
    n2 = float(input("Nota 2: "))
    m = (n1 + n2) / 2
    print("\nMédia:", m)
    if m >= 5:
        print("APROVADO")
        ap += 1
    elif m <= 3:
        print("EXAME")
        ex += 1
    else:
        print("REPROVADO")
        re += 1
print(f"\nAprovados: {ap}\nExame: {ex}\nReprovados: {re}")