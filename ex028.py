from random import randint

num_rand = randint(0, 5)
num_user = int(input('Digite um número de 0 a 5! '))
if num_rand == num_user:
    print('Parabéns, vc acertou, o número escolhido pelo computador também foi {}'.format(num_rand))
else:
    print('Você errou! O número escolhido pelo computador foi {}'.format(num_rand))
