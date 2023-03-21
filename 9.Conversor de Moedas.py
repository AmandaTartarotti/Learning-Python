a = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${:.2f} você pode comprar US${:.2f} e EUR${:.2f}'.format(a, a/5.31, a/6.49))