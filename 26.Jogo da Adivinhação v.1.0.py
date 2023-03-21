import random
import time
pc = random.randint(0, 5) #faz o computador sortear um número
print('-='*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*30)
a = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(2)
if a == pc:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[31mGANHEI! Eu pensei no número {} não {}!'.format(pc, a))
#sempre coloca \033[...m
#primeiro número se refere a estilo 0=none, 1=bold, 4=underline, 7=negative
#segundo número se refere a cor 30=branco, 31=vermelho, 32=verde, 33=amarelo, 34=azul, 35=roxo, 36=ciano, 37=cinza
#terceiro número se refere a back 40=branco, 41=vermelho, 42=verde, 43=amarelo, 44=azul, 45=roxo, 46=ciano, 47=cinza