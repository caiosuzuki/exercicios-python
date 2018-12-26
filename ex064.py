cont = soma = num = 0

while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        soma += num
        cont += 1
print('Você informou {} números e a soma deles é: {}'.format(cont, soma))