class conta_bancaria:
    def __init__(self):
        self.titular = "null"
        self.numero_conta = "null"
        self.saldo_atual = 0
    def depositar(self):
        self.saldo_atual = self.saldo_atual + float(input("deposite um valor: "))
        return self.saldo_atual
    def retirar(self):
        self.saldo_atual = self.saldo_atual - float(input("retire um valor: "))
        return self.saldo_atual
    def verificar(self):
        return self.saldo_atual

x = conta_bancaria()
x.titular = str(input("insira seu nome: "))
x.numero_conta = str(input("insira o numero da conta: "))


y = 999

while y != 0:
    y = int(input("insira um valor, 0 = sair, 1 = depositar, 2 = retirar, 3 = verificar: "))
    if y == 1:
        x.depositar()
    elif y == 2:
        x.retirar()
    elif y == 3:
        print("valor atual da conta",x.numero_conta,"de",x.titular,"=",x.verificar(),"R$")

# valor atual da conta "numero conta" de "nome": valor