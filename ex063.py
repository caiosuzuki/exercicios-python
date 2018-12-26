print('{:=^40}'.format(' Sequência de Fibonacci'))
qt_elem = int(input('Quantos termos quer ver? '))
cont = 0
ant = 0
atual = 1
print('~' * 40)
print(ant, end=' → ')
while cont < qt_elem:
    print('{} →'.format(atual), end=' ')
    aux = atual
    atual = ant + atual
    ant = aux
    cont += 1

print('FIM\n' + '~' * 40)