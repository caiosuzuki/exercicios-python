salario = float(input('Digite o salário do funcionário: '))
if salario > 1250.0:
    mult_salario = 1.1
else:
    mult_salario = 1.15
print('Para um salário de R${:.2f} o aumento é de {:.2f}% e fica R${:.2f}'.format(salario, (mult_salario-1)*100,(mult_salario * salario)))
