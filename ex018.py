import math
angulo = float(input('Digite um ângulo: '))
angrad = math.radians(angulo)
print('O ângulo {} tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, math.sin(angrad), math.cos(angrad), math.tan(angrad)))
