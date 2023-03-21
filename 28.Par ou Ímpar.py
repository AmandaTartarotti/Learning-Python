a = float(input('\033[35mMe diga um número qualquer: '))
if a%2 == 0:
    print('\033[37mO número {}{} {}é PAR'.format('\033[34m', a, '\033[m'))
else:
    print('\033[37mO número {}{} {}é ÍMPAR'.format('\033[34m', a, '\033[m'))
#sempre coloca \033[...m
#primeiro número se refere a estilo 0=none, 1=bold, 4=underline, 7=negative
#segundo número se refere a cor 30=branco, 31=vermelho, 32=verde, 33=amarelo, 34=azul, 35=roxo, 36=ciano, 37=cinza
#terceiro número se refere a back 40=branco, 41=vermelho, 42=verde, 43=amarelo, 44=azul, 45=roxo, 46=ciano, 47=cinza