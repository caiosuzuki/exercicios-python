def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')

print(f'{"Controle de Terrenos":^20}')
print('-'*20)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)