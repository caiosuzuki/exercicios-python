soma_pares = soma_terceira_coluna = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o elemento ({i}, {j}) da matriz: '))
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        if j == 2:
            soma_terceira_coluna += matriz[i][j]

print('~*'*20)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print('~*'*20)

print(f'A soma de todos os pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
