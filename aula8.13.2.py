#Classe eleitoral
#Por Daniels :D

import os
os.system("cls")

print("CÁLCULO DE ELEITORES OBRIGATÓRIOS, FACULTATIVOS E NÃO-ELEITORES")
ne = 0
eo = 0
ef = 0
cont = 1
while cont <= 1000:
    idade = int(input("\nIdade: "))
    while idade <= 0 or idade >= 120:
        print("IDADE INVÁLIDA")
        idade = int(input("\nIdade: "))
    if idade < 16:
        print("Não-Eleitor")
        ne += 1
    elif idade < 18 or idade > 65:
        print("Eleitor facultativo")
        ef += 1
    else:
        print("Eleitor obrigatório")
        eo += 1
    cont += 1
print("\nNão-eleitor:", ne,"\nEleitor facultativo:", ef,"\nEleitor obrigatório:", eo)