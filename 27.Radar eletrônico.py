a = float(input('Qual a velocidade atual do carro? '))
if a > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é 80km/h')
    print('\033[31mVocê deve pagar uma multa de R${:.2f}'.format((a-80)*7))
print('\033[32;1mTenha um bom dia! Dirija com segurança!')
#sempre coloca \033[...m
#primeiro número se refere a estilo 0=none, 1=bold, 4=underline, 7=negative
#segundo número se refere a cor 30=branco, 31=vermelho, 32=verde, 33=amarelo, 34=azul, 35=roxo, 36=ciano, 37=cinza
#terceiro número se refere a back 40=branco, 41=vermelho, 42=verde, 43=amarelo, 44=azul, 45=roxo, 46=ciano, 47=cinza