from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print('Você ainda vai se alistar ao serviço militar! Falta(m) {} ano(s)!'.format(18-idade))
elif idade == 18:
    print('Você deve se alistar esse ano ao serviço militar!')
else:
    print('Seu tempo já passou, tá safe! Você tá safe há {} ano(s)'.format(idade-18))
