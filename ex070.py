total = mais_caros_que_1000 = preco_do_mais_barato = cont = 0
nome_do_mais_barato = ''
while True:
    print('=-='*3 + ' Informe o produto ' + '=-='*3)
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))

    if cont == 0 or preco < preco_do_mais_barato:
        nome_do_mais_barato = nome
        preco_do_mais_barato = preco
    cont += 1

    if preco > 1000:
        mais_caros_que_1000 += 1
    total += preco

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('{:-^40}'.format(' Fim do programa '))
print(f'''Total gasto: R${total:.2f}
Produtos que custam mais que R$1000.00: {mais_caros_que_1000}
Nome do mais barato: {nome_do_mais_barato}''')
