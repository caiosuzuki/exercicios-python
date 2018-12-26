print('{:=^40}'.format(' 10 termos da PA '))
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
s = primeiro_termo
ultimo_termo = primeiro_termo + (10) * razao
for i in range(primeiro_termo, ultimo_termo, razao):
    print(s, end=' ')
    s = s + razao
