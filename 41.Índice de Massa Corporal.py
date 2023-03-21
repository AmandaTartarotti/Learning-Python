a = float(input('Qual é seu peso? (Kg)'))
b = float(input('Qual sua altura? (m)'))
IMC = a / (b**2)
print('O IMC dessa pessoa é {:.2f}'.format(IMC))
print('Você está ', end="")
if IMC < 18.5:
    print('ABAIXO DO PESO normal')
elif IMC < 25:
    print('no peso ideal, PARABÉNS!')
elif IMC < 30:
    print('com SOBREPESO')
elif IMC < 40:
    print('com OBESIDADE')
else:
    print('com OBESIDADE MORBIDA, CUIDADO!')