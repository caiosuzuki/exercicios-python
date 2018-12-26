valores = []
while True:
    num = int(input('Digite um valor:'))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print('~' * 40)
valores.sort()
print(f'Você digitou os valores {valores}')
