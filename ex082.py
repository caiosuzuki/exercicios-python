valores = []
impares = []
pares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Você digitou a lista: {valores}.')
print(f'Você digitou os pares: {pares}.')
print(f'Você digitou os ímpares: {impares}.')
