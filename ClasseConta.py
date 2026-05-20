class Conta:
    def __int__(self, nome, saldo, numero ):
        self.nome = nome
        self.saldo = saldo
        self.numero = numero
    def saca(self, valor):
       if 0 < valor <= self.saldo:
           self.saldo -= valor
           print("saque de R$",valor, "foi efetuado com sucesso!")
       else: 
           print("Saldo insuficiente, pobre!")
    def deposita(self, valor):
        if 0 < valor:
            self.saldo += valor
            print("Depósito de R$",valor, "efetuado com sucesso!")
        else:
            print("Não é possível depositar esse valor!")
    def calcularend(self):
        return self.saldo * 0.1

