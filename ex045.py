from random import choice

print('-=-'*3)
print('Jokenpô')
print('-=-'*3)
jogadas = ['pedra', 'papel', 'tesoura']
jogada_do_computador = choice(jogadas)
jogada_do_jogador = str(input('Informe sua jogada: ')).lower().strip()

if jogada_do_jogador == 'pedra':
    if jogada_do_computador == 'pedra':
        print('Empatou! O computador também jogou {}'.format(jogada_do_jogador))
    elif jogada_do_computador == 'papel':
        print('Perdeu! O computador jogou {}'.format(jogada_do_computador))
    else:
        print('Ganhou! O computador jogou {}'.format(jogada_do_computador))
elif jogada_do_jogador == 'papel':
    if jogada_do_computador == 'papel':
        print('Empatou! O computador também jogou {}'.format(jogada_do_jogador))
    elif jogada_do_computador == 'tesoura':
        print('Perdeu! O computador jogou {}'.format(jogada_do_computador))
    else:
        print('Ganhou! O computador jogou {}'.format(jogada_do_computador))
elif jogada_do_jogador == 'tesoura':
    if jogada_do_computador == 'tesoura':
        print('Empatou! O computador também jogou {}'.format(jogada_do_jogador))
    elif jogada_do_computador == 'pedra':
        print('Perdeu! O computador jogou {}'.format(jogada_do_computador))
    else:
        print('Ganhou! O computador jogou {}'.format(jogada_do_computador))
else:
    print('Digite uma jogada válida!')
