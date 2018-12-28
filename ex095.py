dados_jogadores = list()
gols = list()

# Inserindo dados dos jogadores
while True:
    dados_jogador = dict()
    nome = str(input('Nome do jogador: '))
    dados_jogador['nome'] = nome
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    gols.clear()
    for i in range(0, partidas):
        gols_na_partida = int(input(f'Quantos gols na partida {i}? '))
        gols.append(gols_na_partida)
    dados_jogador['gols'] = gols[:]
    dados_jogador['total'] = sum(gols)
    dados_jogadores.append(dados_jogador.copy())

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

# Tabela geral
print('-=' * 30)
print('Cód. ', end='')
for i in dados_jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(dados_jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

# Detalhes de cada jogador
while True:
    print('-' * 50)
    escolhido = int(input('Mostrar dados de qual jogador? '))
    if escolhido == 999:
        print('Finalizando programa.')
        break
    elif escolhido < 0 or escolhido > (len(dados_jogadores) - 1):
        print('Erro! Esse jogador não existe!')
    else:
        print(f'-- Levantamento do jogador {dados_jogadores[escolhido]["nome"]}:')
        for k, v in enumerate(dados_jogadores[escolhido]['gols']):
            print(f'    => Na partida {k}, fez {v} gols.')
