from ContaBancos import ContaCorrente, CartaoCredito

##programa
conta_jonas = ContaCorrente('Jonas', '000.000.000-00', 1234, 111)
conta_amanda = ContaCorrente('Amanda', '000000', '0001', 1112)

cartao_jonas = CartaoCredito('Jonas', conta_jonas)

print(cartao_jonas.numero)
print(cartao_jonas.cod_seguranca)

print(cartao_jonas.senha)
cartao_jonas.senha = '1234a'

print(conta_jonas.__dict__)

print(conta_jonas.__doc__)
