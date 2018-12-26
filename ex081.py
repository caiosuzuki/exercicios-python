valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram digitados {len(valores)} valores.')
valores.sort(reverse=True)
print(f'A lista decrescente fica: {valores}')
if 5 in valores:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')