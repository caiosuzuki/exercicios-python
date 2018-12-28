def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número o qual se deseja o fatorial
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de n.
    """
    fat = 1
    for corrente in range(n, 0, -1):
        if show:
            print(f'{corrente} ', end='')
            print('= ' if corrente == 1 else 'x ', end='')
        fat *= corrente
    return fat

help(fatorial)
print(fatorial(5, show=True))
