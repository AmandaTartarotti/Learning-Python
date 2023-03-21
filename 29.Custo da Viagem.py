a = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(a))
preço = a*0.5 if a <= 200 else a*0.45
print('E o preço da sua passagem será de R${}'.format(preço))

'''if a <= 200:
    print('E o preço da sua passagem será de R${}'.format(a*0.5))
else:
    print('E o preço da sua passagem será de R${}'.format(a*0.45))'''