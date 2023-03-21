galera = list()
dado = list()
pesado = []
leve = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0:
        menor = maior = dado[1]
    galera.append(dado[:])
    dado.clear()
    c = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if c == 'n':
        break
for p in galera:
    if p[1] == maior:
        pesado.append(p[0])
    elif p[1] > maior:
        maior = p[1]
        pesado.clear()
        pesado.append(p[0])
    elif p[1] == menor:
        leve.append(p[0])
    elif p[1] < menor:
        menor = p[1]
        leve.clear()
        leve.append(p[0])
print('='*30)
print(f'Ao todo você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de {pesado}')
print(f'O menor peso foi de {menor}Kg. Peso de {leve}')