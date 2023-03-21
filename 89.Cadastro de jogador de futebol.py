dados = {}
gols = []
total = 0
dados['Nome'] = str(input('Nome da jogadora: '))
partidas = int(input(f'Quantas partidadas {dados["Nome"]} jogou? '))
for i in range(0,partidas):
    a = (int(input(f'Quantos gols na partida {i}? ')))
    total += a
    gols.append(a)
dados['Gols'] = gols[:]
dados['Total'] = total
print('-='*30)
print(dados)
print('-='*30)
for i, v in dados.items():
    print(f'O campo {i} tem valor {v}')
print('-='*30)
print(f'A jogadora {dados["Nome"]} jogou {partidas} partidas.')
for i in range(0, partidas):
    print(f'     -> Na partida {i}, fez {dados["Gols"][i]} gols.')