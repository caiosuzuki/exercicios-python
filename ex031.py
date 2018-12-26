dist = float(input('Digite a distância da viagem em km: '))
if dist <= 200.0:
    print('Será cobrado R$0,50 por km! Sua passagem custará R${:.2f}'.format(dist*0.5))
else:
    print('Será cobrado R$0,45 por km! Sua passagem custará R${:.2f}'.format(dist * 0.45))
