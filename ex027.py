nome_completo = str(input('Digite seu nome completo: '))
print('Muito prazer em te conhecer!')
nome_splitado = nome_completo.split()
print('Seu primeiro nome é: {}'.format(nome_splitado[0]))
print('Seu último nome é: {}'.format(nome_splitado[len(nome_splitado)-1]))
