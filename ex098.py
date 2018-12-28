from time import sleep


def mostra_linha_enfeitada():
    print('-=' * 20)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    mostra_linha_enfeitada()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio > fim:
        passo = -passo
    corrente = inicio
    continua = True
    while continua:
        print(f'{corrente} ', end='', flush=True)
        sleep(0.25)
        corrente += passo
        if passo > 0 and corrente > fim:
            continua = False
        elif passo < 0 and corrente < fim:
            continua = False
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
