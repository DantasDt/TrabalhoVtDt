class Conta:
    def _init_(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    def saca(self, valor):
       if 0 < valor <= self.saldo:
           self.saldo -= valor
           print("saque de R$",valor, "foi efetuado com sucesso!")
           print("Saldo atual: ", self.saldo)
       else: 
           print("Saldo insuficiente, pobre!")
    def deposita(self, valor):
        if 0 < valor:
            self.saldo += valor
            print("Depósito de R$",valor, "efetuado com sucesso!")
            print("Saldo atual: ", self.saldo)
        else:
            print("Não é possível depositar esse valor!")
    def calcularend(self):
        print("Rendimento mensal: ", self.saldo * 0.1)
