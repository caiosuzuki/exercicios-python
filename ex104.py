from colorama import Fore
from colorama import Style


def leia_int(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print(f'{Fore.RED}ERRO! Digite um número inteiro válido.{Style.RESET_ALL}')


n = leia_int('Digite um número: ')
print(f'Você digitou o número {n}.')

