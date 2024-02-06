#Tabuada
#Por Daniels :D

import os
os.system("cls")

resp = "S"
while resp == "S":
    print("TABUADA")
    num = int(input("\nNúmero: "))
    print()
    cont = 1
    while cont <= 10:
        r = num * cont
        print(num, "*", cont, "=", r)
        cont += 1
    resp = input("\nDeseja escolher outro número? S/N: ").upper
    while resp != "S" and resp != "N":
        resp = input("\nOpção inválida.\nDeseja escolher outro número? S/N: ").upper
print("\nObrigado por utilizar esse programa :D")