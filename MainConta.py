import os
os.system("cls")
from ClasseConta import Conta
nome = str(input("Informe seu nome: "))
saldo = float(input("Informe o saldo: "))
obj = Conta(nome, saldo)
while True:
    print("Oque deseja fazer?")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Ver rendimento")
    print("4. Sair")
    p1 = int(input(""))
    if p1 != 1 and p1 != 2 and p1 != 3 and p1 != 4:
        print("Valor invalido")
    elif p1 == 4:
        break
    elif p1 == 1:
        valor = float(input("Informe o valor para sacar: "))
        os.system("cls")
        obj.saca(valor)
        print("")
    elif p1 == 2:
        valor = float(input("Informe o valor para depositar: "))
        os.system("cls")
        obj.deposita(valor)
        print("")
    elif p1 == 3:
        os.system("cls")
        print(obj.calcularend())
