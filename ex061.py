primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
atual = primeiro_termo
print('Os 10 primeiros termos da PA são: ')
while cont <= 10:
    print(atual, end=' ')
    atual += razao
    cont += 1
