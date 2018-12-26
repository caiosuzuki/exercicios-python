maiores_de_18 = qt_homens = mulheres_abaixo_de_20 = 0

while True:
    print('~-~'*3 + ' Cadastre uma pessoa ' + '~-~'*3)
    idade = int(input('Informe a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo da pessoa [M/F]: ')).strip().upper()[0]

    if idade > 18:
        maiores_de_18 += 1
    if sexo == 'M':
        qt_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_abaixo_de_20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'''Você informou {maiores_de_18} maior(es) de 18 anos,
{qt_homens} homens e 
{mulheres_abaixo_de_20} mulher(es) abaixo de 20 anos.''')
