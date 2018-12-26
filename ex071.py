print('=' * 40)
print('{:^40}'.format('Banco do Bujão'))
print('=' * 40)

valor_saque = int(input('Informe o valor a ser sacado: R$'))
notas = 0

valores_notas = [50, 20, 10, 1]

for valor_nota in valores_notas:
    notas = valor_saque // valor_nota
    valor_saque = valor_saque - notas * valor_nota
    print(f'Total de {notas:.0f} cédulas de R${valor_nota}')
print('Volte sempre ao Banco do Bujão! Tenha um bom dia!')
