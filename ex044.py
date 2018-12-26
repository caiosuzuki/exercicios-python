print('{:=^40}'.format(' LOJAS BUJAOZINHO '))
preco_normal = float(input('Informe o preço normal do produto: R$'))
cond_pagamento = str(input('Informe a condição de pagamento (dinheiro, cheque ou cartão): ')).strip()
if cond_pagamento == 'cartão':
    parcelas = int(input('Informe quantas parcelas quer realizar: '))

if cond_pagamento == 'dinheiro' or 'cheque':
    preco = preco_normal * 0.9
elif cond_pagamento == 'cartão':
    if parcelas == 1:
        preco = preco_normal * 0.95
    elif parcelas == 2:
        preco = preco_normal
    else:
        preco = preco_normal * 1.2
else:
    print('Digite uma condição de pagamento válida!')
print('O preço a pagar será R${:.2f}'.format(preco))