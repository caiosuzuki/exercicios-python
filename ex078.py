valores = []
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'Os valores digitados foram {valores}')
maior = max(valores)
menor = min(valores)
print(f'O menor valor foi {menor} nas posições', end=' ')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}', end='...')
print(f'\nO menor valor foi {maior} nas posições', end=' ')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}', end='...')
