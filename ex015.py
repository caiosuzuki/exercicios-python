km = float(input('Informe quantos km o carro alugado rodou: '))
dias = int(input('Informe quantos dias ele foi alugado: '))
preco = 60*dias + 0.15*km
print('O preço a pagar por {} dias e {} km rodados é R${:.2f}'.format(dias, km, preco))
