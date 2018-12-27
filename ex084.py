pessoas = list()
dados = list()
peso_leve = 0
peso_pesado = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        peso_leve = peso_pesado = dados[1]
    else:
        if dados[1] > peso_pesado:
            peso_pesado = dados[1]
        if dados[1] < peso_leve:
            peso_leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {peso_pesado:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == peso_pesado:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {peso_leve:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == peso_leve:
        print(f'[{p[0]}]', end=' ')
