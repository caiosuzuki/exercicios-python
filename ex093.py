dados_jogador = dict()
nome = str(input('Nome do jogador: '))
dados_jogador['nome'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou? '))
gols = list()
for i in range(0, partidas):
    gols_na_partida = int(input(f'Quantos gols na partida {i}? '))
    gols.append(gols_na_partida)
dados_jogador['gols'] = gols[:]
dados_jogador['total'] = sum(gols)

print('-='*30)
print(dados_jogador)
print('-='*30)

for k, v in dados_jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)

print(f'O jogador {dados_jogador["nome"]} jogou {len(dados_jogador["gols"])} partidas.')
for k, v in enumerate(dados_jogador['gols']):
    print(f'    => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {dados_jogador["total"]} gols.')
