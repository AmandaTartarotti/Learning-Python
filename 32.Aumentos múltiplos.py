a = float(input('Qual é o salário do funcionário? '))
if a > 1250:
    print('Quem ganhava R${} passa a ganhar {} agora.'.format(a, a + a*0.1))
else:
    print('Quem ganhava R${} passa a ganhar {} agora.'.format(a, a + a*0.15))