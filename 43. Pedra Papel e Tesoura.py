import random
import time
print('''Suas opções:
[0] PEDRA 
[1] PAPEL 
[2] TESOURA''')
a = int(input('Qual sua escolha? '))
if a != 0 and a != 1 and a != 2:
    print('Insira número váido')
else:
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    time.sleep(1)
    print('-='*12) 
    computador = random.randint(0,2)
    b = ('Pedra', 'Papel', 'Tesoura')
    print('Computador jogou {}'.format(b[computador]))
    print('Jogador jogou {}'.format(b[a]))
    print('-='*12)
    if a == computador:
        print('\033[34mEMPATE')
    elif a == 0 and computador == 2:
        print('\033[32mVOCÊ VENCEU')
    elif a == 0 and computador == 1:
        print('\033[31mEU VENCI!')
    elif a == 1 and computador == 2:
        print('\033[31mEU VENCI!')
    elif a == 1 and computador == 0:
        print('\033[32mVOCÊ VENCEU')
    elif a == 2 and computador == 0:
        print('\033[31mEU VENCI!')
    else:
        print('\033[32mVOCÊ VENCEU')