valores = []
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        for p, v in enumerate(valores):
            if v > num:
                valores.insert(p, num)
                print(f'Adicionado na posição {p} da lista...')
                break

print(f'Os valores em ordem foram: {valores}')
