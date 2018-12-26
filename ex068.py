from random import randint

print('-=-' * 10)
print('Par ou ímpar')
print('-=-' * 10)

vitorias = 0

while True:
    mao_jogador = int(input('Diga um valor: '))
    p_ou_i = ' '
    while p_ou_i not in 'PI':
        p_ou_i = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    mao_computador = randint(0, 5)
    soma = mao_jogador + mao_computador

    if (soma % 2 == 0 and p_ou_i == 'P') or (soma % 2 == 1 and p_ou_i == 'I'):
        venceu = True
        vitorias += 1
    else:
        venceu = False

    print(f'Você jogou {mao_jogador} e o computador jogou {mao_computador}. Total de {soma}')
    print('Deu par!' if soma % 2 == 0 else 'Deu ímpar!')

    if not venceu:
        break
    print('Você venceu, vamos jogar novamente! ')

print(f'Game over, você venceu {vitorias} vez(es) antes de perder.')
