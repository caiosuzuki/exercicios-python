maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa (kg): '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('O menor peso foi {}kg e o maior peso foi {}kg'.format(menor, maior))
