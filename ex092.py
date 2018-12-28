from datetime import date

nome = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
ctps = int(input('Carteira de trabalho (0 não tem): '))
pessoa = {'nome': nome, 'idade': idade, 'ctps': ctps}
if ctps != 0:
    pessoa['ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    idade_contratado = pessoa['ano de contratação'] - ano_nasc
    pessoa['aposentadoria'] = idade_contratado + 35

print('~'*50)
for k, v in pessoa.items():
    print(f'{k} tem valor {v}.')
