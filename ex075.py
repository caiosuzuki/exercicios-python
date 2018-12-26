n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
n4 = int(input('Quarto valor: '))

valores = (n1, n2, n3, n4)
print(f'Os valores digitados foram {valores}.')
print(f'O número 9 apareceu {valores.count(9)} vez(es).')
if 3 in valores:
    print(f'O primeiro 3 foi digitado na posição {valores.index(3)+1}.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram:', end=' ')
for i in range(0, 4):
    if valores[i] % 2 == 0:
        print(f'{valores[i]}', end=' ')
