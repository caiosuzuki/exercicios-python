s = 0
for num in range(0, 501, 3):
    if num % 2 == 1:
        s = s + num
print('A soma dos números múltiplos de 3 e ímpares entre 1 e 500 é: {}'.format(s))