#Tabuada
#Por Daniels :D

import os
os.system("cls")

resp = "S"
while resp == "S":
    print("\nTABUADA")
    num = int(input("\nNúmero: "))
    print()
    for cont in range(1, 11):
        r = num * cont
        print(num, "*", cont, "=", r)
    resp = input("\nDeseja escolher outro número? S/N: ").upper()
    while resp != "S" and resp != "N":
        resp = input("\nOpção inválida.\nDeseja escolher outro número? S/N: ").upper()
print("\nObrigado por utilizar esse programa :D")