##Crie uma classe chamada "ContaBancaria"
##que tenha os atributos "titular" e "saldo". Crie
##métodos para depositar, sacar e exibir o saldo da
##conta.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular=titular
        self.saldo=saldo
    def depositar(self, valor):
        self.saldo+=valor
    def sacar(self, valor):
        if self.saldo>=valor:
            self.saldo-=valor
        else:
            print("Saldo insuficiente")
    def exibir_saldo(self):
        print(f"O saldo é de {self.saldo}")

conta = ContaBancaria("João")

conta.depositar(50)
conta.sacar(40)
conta.exibir_saldo()
