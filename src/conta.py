class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def sacar(self, saque):
        saldo_com_limite = self.con_saldo()

        if saque > saldo_com_limite:
            print(f'Saldo insuficiente. Seu saldo atual é de: R$ {saldo_com_limite}')
        else:
            self.saldo -= saque
            print(f'Saque realizado no valor de R$ {saque}. Seu saldo atual é de R$ {saldo_com_limite}.')

    def depositar(self, deposito):
        self.saldo += deposito
        saldo_com_limite = self.con_saldo()
        print(f'Deposito realizado com sucesso. Seu saldo atual é de R$ {saldo_com_limite}')


    def con_saldo(self):
        saldo_com_limite = self.saldo + self.limite
        return saldo_com_limite
