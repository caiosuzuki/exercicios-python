nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
if media < 5.0:
    situacao = 'reprovado'
elif media < 7.0:
    situacao = 'recuperação'
else:
    situacao = 'aprovado'
aluno = {'Nome': nome, 'Média': media, 'Situação': situacao}

for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
