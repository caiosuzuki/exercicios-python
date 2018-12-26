cont = soma = 0
print('Pare o programa com 999 a qualquer momento!')
while True:
    n = int(input('Digite um inteiro: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} inteiros informados é {soma}')