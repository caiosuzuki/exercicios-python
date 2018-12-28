
def voto(ano_de_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual -ano_de_nascimento
    if idade < 16:
        return f'Com {idade} anos, o voto é negado.'
    elif idade < 18 or idade >= 65:
        return f'Com {idade} anos, o voto é opcional.'
    else:
        return f'Com {idade} anos, o voto é obrigatório.'

print('-'*30)
ano_de_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_de_nascimento))