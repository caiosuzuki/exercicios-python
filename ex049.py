print('{:=^20}'.format(' Tabuada '))
num = int(input('Digite um número: '))
for mult in range(1, 11):
    print('{} x {:2} = {}'.format(num, mult, num * mult))