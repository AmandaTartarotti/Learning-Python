a = int(input('Quantos dias alugados? '))
b = float(input('Quantos Km rodados? '))
print('O total a pagar é de R${:.2f}'.format(a*60 + 3/20*b)) #podia ser 0.15*b