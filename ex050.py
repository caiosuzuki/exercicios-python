s = 0
for i in range(0, 6):
    n = int(input('Digite um inteiro: '))
    if n % 2 == 0:
        s += n
print('A soma dos números pares que você digitou é: {}'.format(s))