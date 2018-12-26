primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
atual = primeiro_termo
print('Os 10 primeiros termos da PA são: ')
termos = 10
while cont < termos:
    print('{} →'.format(atual), end=' ')
    atual += razao
    cont += 1
    if cont == termos:
        termos = int(input('\nQuer ver mais quantos termos? '))
        cont = 0
