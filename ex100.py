from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range (0, 5):
        n = randint(1, 10)
        print(f'{n} ', end='', flush=True)
        sleep(0.25)
        lista.append(n)
    print('Pronto!')

def somaPar(valores):
    s = 0
    for v in valores:
        if v % 2 == 0:
            s += v
    print(f'A soma dos pares da lista {valores} é {s}.')

numeros = list()
sorteia(numeros)
somaPar(numeros)