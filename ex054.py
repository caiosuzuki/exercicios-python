from datetime import date

maiores = 0
ano_atual = date.today().year
for i in range(1, 8):
    ano_nasc_pessoa = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    if ano_atual - ano_nasc_pessoa >= 18:
        maiores += 1
print('Nesse grupo de pessoas tem {} menor(es) e {} maior(es)'.format(7 - maiores,  maiores))

## esse ex ta dano ruim acho q é pq a lista deu coco