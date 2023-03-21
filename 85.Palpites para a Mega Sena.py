from random import randint
from time import sleep
print('-'*20)
print(f'JOGA NA MEGA SENA'.center(20))
print('-'*20)
a = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*5, f'SORTENADO {a} JOGOS', '-='*5)
lista = list()
for i in range(1,a+1):
    count = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count == 6:
            break
    print(f'O jogo {i}:', lista)
    sleep(1)
    lista.clear()
print('-='*5, 'BOA SORTE', '-='*5)