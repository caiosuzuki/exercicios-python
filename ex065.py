cont = soma = maior = menor = 0
r = 'S'

while r == 'S':
    num = int(input('Digite um número inteiro: '))
    if cont == 0:
        menor = num
        maior = num
    soma += num
    cont += 1
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    r = str(input('Quer continuar? [S/N] ')).upper().strip()

print('Você informou {} números e a média deles é: {:.2f}'.format(cont, soma / cont))
print('O menor deles foi {} e o maior deles foi {}'.format(menor, maior))
