print('-=-'*8)
print('Analisador de Triângulos')
print('-=-'*8)
c1 = float(input('Digite o comprimento da primeira reta: '))
c2 = float(input('Digite o comprimento da segunda reta: '))
c3 = float(input('Digite o comprimento da terceira reta: '))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Essas três retas formam um triângulo!')
else:
    print('Essas três retas NÃO formam um triângulo!')
