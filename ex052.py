print('{:=^40}'.format(' Número primo? '))
num = int(input('Digite um número '))
for i in range(2, num+1):
    if i == num:
        print('Esse número é primo!')
        break
    if num % i == 0:
        print('Esse número não é primo!')
        break
