from time import sleep


def maior(*valores):
    maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for i, v in enumerate(valores):
        print(f'{v} ', end='', flush=True)
        sleep(0.25)

        if i == 0:
            maior = v
        else:
            if v > maior:
                maior = v
    print(f'\nForam informados {len(valores)} valores ao todo.')
    print(f'O maior valor foi o {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
