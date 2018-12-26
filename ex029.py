vel = int(input('Digite a velocidade do carro em km/h: '))
if vel > 80:
    excedido = vel - 80
    print('Você foi multado! O limite de velocidade é 80km/h,\n'
          'a multa é de R${:.2f} por passar {}% do limite '
          'de velocidade'.format(excedido * 7, excedido/80*100))
else:
    print('Você está dentro do limite de velocidade!')
