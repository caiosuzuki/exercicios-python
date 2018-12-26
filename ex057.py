sexo = 'invalido'
sexo = str(input('Digite o sexo [M/F]: '))
while sexo not in 'MF':
    sexo = str(input('Dado inválido. Digite o sexo [M/F]: '))
print('Ok, vocẽ escolheu o sexo {}'.format(sexo))