from random import randint
from random import randint
from time import sleep
números = []
def sorteia():
    for i in range(0,5):
        a = randint(0,10)
        números.append(a)
        a = 0
    print(f'Sorteando 5 valores da lista: ', end=" ")
    for j in números:
        print(j, end= " ", flush=True)
        sleep(0.5)
    print('PRONTO!')
def somaPar():
    soma = 0
    for k in números:
        if k % 2 == 0:
            soma += k
    print('Somando os valores pares de {}, temos {}'.format(números, soma))

sorteia()
somaPar()