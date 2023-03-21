from random import randint
from typing import Counter
a = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))    
print('Os valores sorteados foram', end=" ")
for n in a:
    print(f'{n}', end=' ')
print('\nO maior valor foi {}'.format(max(a))) # \n faz pular pra linha de baixo
print('O menor valor foi {}'.format(min(a)))
#min e max são fuções de tuplas 