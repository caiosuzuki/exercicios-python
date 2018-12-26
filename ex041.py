from datetime import date
ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano_de_nascimento
if idade <= 9:
    categoria = 'mirim'
elif idade <= 14:
    categoria = 'infantil'
elif idade <= 19:
    categoria = 'júnior'
elif idade <= 25:
    categoria = 'sênior'
else:
    categoria = 'master'
print('Sua categoria é {}'.format(categoria))