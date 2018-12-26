print('{:=^40}'.format(' Analisador de palíndromo '))
frase = input('Digite uma frase qualquer: ').upper()
splitada = frase.split()
frase = ''.join(splitada)
for i in range(0, int(len(frase) / 2)):
    if frase[i] != frase[len(frase) - i - 1]:
        print('Essa frase não é um palíndromo!')
        exit(0)
print('Essa frase é um palíndromo!')
