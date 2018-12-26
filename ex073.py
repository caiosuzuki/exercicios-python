times = ('palmeiras', 'flamengo', 'internacional', 'grêmio',
             'são paulo', 'atlético-mg', 'atlético-pr', 'cruzeiro',
             'botafogo', 'santos', 'bahia', 'fluminense', 'corinthians',
             'chapecoense', 'ceará', 'vasco', 'sport', 'américa-mg',
             'vitória', 'paraná')
print(f'Os 20 times colocados são: {times}')
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'O chapecoense está na {times.index("chapecoense")+1}ª posição.')
