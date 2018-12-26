produtos_e_precos = (('Pão', 1.0), ('Caneta', 2.0),
                     ('Tesoura', 4.5), ('Bolo', 20.0),
                     ('Caixa de som', 50.0), ('Caneca', 10.0))
print('~'*40)
print('{:^40}'.format(' Loja do bujão '))
print('~'*40)

for pp in produtos_e_precos:
    print(f'{pp[0]:.<30}', end='')
    print(f'R${pp[1]:>7.2f}')
