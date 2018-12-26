soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
qt_mulheres_abaixo_de_20_anos = 0
for p in range (1,5):
    print('----- {}ª pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade

    if maior_idade_homem < idade and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        qt_mulheres_abaixo_de_20_anos += 1

media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_homem_mais_velho))
