pessoas = list()
soma_idades = 0
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    idade = int(input('Idade: '))
    soma_idades += idade
    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(pessoa.copy())

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
media_idade = soma_idades / len(pessoas)
print('-=' * 40)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media_idade:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print(f'- Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > media_idade:
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
