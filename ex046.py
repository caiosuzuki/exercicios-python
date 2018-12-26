from time import sleep

print('{:=^40}'.format(' Contagem Regressiva '))
for i in range(10, -1, -1):
    print('{:^40}'.format(i))
    sleep(1)
print('{:^40}'.format('Feliz ano novo!!!'))