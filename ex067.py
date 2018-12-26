while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for mult in range(1, 11):
        print(f'{n} x {mult} = {n * mult}')
print('Fim do programa.')
