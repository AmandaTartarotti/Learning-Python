dados = {}
lista = list()
gols = []
while True:
    total = 0
    dados['Nome'] = str(input('Nome da jogadora: '))
    partidas = int(input(f'Quantas partidadas {dados["Nome"]} jogou? '))
    for i in range(0,partidas):
        a = (int(input(f'Quantos gols na partida {i}? ')))
        total += a
        gols.append(a)
    dados['Gols'] = gols[:]
    dados['Total'] = total
    lista.append(dados.copy())
    dados.clear()
    gols.clear()
    resp = str(input('Quer continuar? [S/N]' ))
    if resp == 'n':
        break
print('-='*30)
print(f'{"cod":<10}{"nome":<10}{"gols":<10}{"total":<10}')
print('-'*30)
for c, v in enumerate(lista):
    print(f'\n{c:<10}', end="")
    for d in v.values():
        print(f'{str(d):<10}', end="")
print()
while True:
    print(f''*70)
    b = int(input('Mostrar a perfomace de qual jogador? (999 interrompe) '))
    if b == 999:
        break
    for c, v in enumerate(lista):
        if b == c:
            print('LEVANTAMENTO DA JOGADORA {}:'.format(v["Nome"]))
            for i, g in enumerate(lista[b]["Gols"]):
                print(f'No jogo {i+1} fez {g} gols.')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
