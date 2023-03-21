from time import sleep
from random import randint
from operator import itemgetter
dados = {}
ranking = []
for i in range(1,5):
    dados[f'jogador{i}'] = randint(0,6)
print('Valores sorteados:')
for i, v in dados.items():
    print(f'{i} tirou {v} no dado.')
    sleep(1)
print('-='*20)
print('== RANKING DOS JOGADORES ==')
ranking = sorted(dados.items(), key=itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)