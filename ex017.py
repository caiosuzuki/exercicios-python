from math import hypot
catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(catop, catad)
print('A hipotenusa do triângulo retângulo com cateto oposto de {} e cateto adjacente {} é {:.2f}'.format(catop, catad, hip))
