print('-=-'*8)
print('Analisador de Triângulos')
print('-=-'*8)
c1 = float(input('Digite o comprimento do primeiro segmento: '))
c2 = float(input('Digite o comprimento do segundo segmento: '))
c3 = float(input('Digite o comprimento do terceiro segmento: '))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Esses três segmentos formam um triângulo!')
    if c1 == c2 == c3:
        print('Esse triângulo será equilátero!')
    elif c1 == c2 or c2 == c3 or c1 == c3:
        print('Esse triângulo será Isósceles!')
    else:
        print('Esse triângulo será escaleno!')
else:
    print('Esses três segmentos NÃO formam um triângulo!')
