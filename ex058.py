from random import randint

n_palpites = 1
num_escolhido_pelo_computador = randint(0, 11)
num_jogador = int(input('Tente um número de 1 a 10: '))

while num_jogador != num_escolhido_pelo_computador:
    num_jogador = int(input('Tente adivinhar de novo: '))
    n_palpites += 1
print('Parabéns, vc adivinhou depois de {} palpites o número {} que o computador sorteou.'.format(n_palpites, num_escolhido_pelo_computador))
