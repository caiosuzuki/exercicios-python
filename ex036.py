casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Informe seu salário: R$'))
anos = int(input('Em quantos anos quer pagar? '))
prestacao = casa / (anos * 12)
if prestacao > salario * 0.3:
    print('Empréstimo negado! O valor da prestação (R${:.2f}) excede 30% do seu salário'.format(prestacao))
else:
    print('Seu empréstimo foi aprovado!')
