num = int(input('Informe um número inteiro: '))
print("""Escolha a base de conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal""")
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Informe uma opção válida!')