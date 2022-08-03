from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
        self._caixa_minino = 1_000_000

    def verificar_caixa(self):
        if self.caixa < self._caixa_minino:
            print(f'Caixa abaixo no nível recomendado. Caixa atual: R${self.caixa:,.2f}')
        else:
            print(f'Valor atual do caixa: R${self.caixa:,.2f}\n')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            self.caixa -= valor

    def adicionar_clientes(self, nome, cfp, patrimonio):
        self.clientes.append((nome, cfp, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1_000_000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        if valor <= self.caixa:
            self.caixa -= valor
            self.caixa_paypal += valor
        else:
            print('saldo insuficiente para realizar a transação')

    def sacar_paypal(self, valor):
        if valor <= self.caixa_paypal:
            self.caixa_paypal -= valor
            self.caixa += valor
        else:
            print('saldo insuficiente para realizar a transação')


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super(AgenciaComum, self).__init__(telefone, cnpj, numero = randint(1001, 9999))
        self.caixa = 1_000_000


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10_000_000

    def adicionar_clientes(self, nome, cfp, patrimonio):
        if patrimonio > 1_000_000:
            super().adicionar_clientes(nome, cfp, patrimonio)
            print(f'Seja bem vindo {self.clientes[0][0]}!')
        else:
            print('Perfil do cliente não condiz com este tipo de agência.')


## Teste classes

print('*' * 15 + ' Agência Virtual ' + '*' * 15 + '\n')

ag_virtual = AgenciaVirtual('www.siteagencia.com.br', 444444444, 13132434343)
ag_virtual.verificar_caixa()
ag_virtual.depositar_paypal(1_000_000)
ag_virtual.verificar_caixa()
ag_virtual.depositar_paypal(1_000_001)
print()

print('*' * 15 + ' Agência Comum ' + '*' * 15 + '\n')

ag_comum = AgenciaComum(22222, 55151143)
ag_comum.verificar_caixa()
print()

print('*' * 15 + ' Agência Premium ' + '*' * 15 + '\n')

ag_premium = AgenciaPremium(4444,313152154)
print(ag_premium.clientes)
ag_premium.verificar_caixa()

ag_premium.adicionar_clientes('Jonas', 41564313453, 1_000_001)
print(ag_premium.clientes)
