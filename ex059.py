from time import sleep
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

op = 0
while op != 5:
    print('''---- Menu ----
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    op = int(input('Sua opção: '))

    if op == 1:
        print('A soma de {} e {} é {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A multiplicação de {} e {} é {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior entre {} e {} é {}'.format(n1, n2, maior))
    elif op == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    elif op == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida, tente novamente!')
print('Fim do programa, até mais!')