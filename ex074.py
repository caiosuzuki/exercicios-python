from random import randint

n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)

numeros = (n1, n2, n3, n4, n5)

maior = max(numeros)
menor = min(numeros)

print(f'A tupla sorteada foi {numeros}. \nO menor número é o {menor} e o maior é o {maior}.')
