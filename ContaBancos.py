from datetime import datetime
from typing import Type

import pytz
from random import randint


class ContaCorrente:
    """

    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m,%Y %H:%M:%S')

    # construtor xD
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._extrato = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f'Saldo atual de R${self._saldo:,.2f}')

    def depositar(self, valor):
        self._saldo += valor
        self._extrato.append((valor, self._saldo, ContaCorrente._data_hora()))
        self.consultar_saldo()

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def consulta_limite_conta(self):
        print(f'O limmite da conta é de {self._limite}')

    def sacar(self, valor):
        if (self._saldo - valor) < self._limite_conta():
            print('saldo insuficiente.')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self.consultar_saldo()
            self._extrato.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_extrato(self):
        print('=-' * 30)
        print('Extrato da conta conrrente:')
        for transacao in self._extrato:
            print(transacao)

    def transferir(self, valor, conta_destino):
        if (self._saldo - valor) < self._limite_conta():
            print('saldo insuficiente.')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._extrato.append((-valor, self._saldo, ContaCorrente._data_hora()))
            conta_destino._saldo += valor
            conta_destino._extrato.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.cod_seguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova senha inválida')
