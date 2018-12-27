from random import randint
print('-'*40)
print('{:^40}'.format('JOGA NA MEGA SENA'))
print('-'*40)

jogos = list()
qt_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, qt_jogos):
    jogo = list()
    for j in range(0, 6):
        num_rand = randint(1, 60)
        while num_rand in jogo:
            num_rand = randint(1, 60)
        jogo.append(num_rand)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

for p, j in enumerate(jogos):
    print(f'Jogo {p+1}: {j}')
