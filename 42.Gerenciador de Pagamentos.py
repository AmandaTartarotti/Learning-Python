print('{:=^40}'.format('LOJAS AMANDAS'))
a = float(input('Preço das compras: '))
print('FORMA DE PAGAMENTO')
print('[1] à vista dinheiro')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
b = float(input('Qual a opção? '))
if b == 1:
    print('Sua compra de {} vai custar {} no final.'.format(a, a - a*0.1))
elif b == 2:
    print('Sua compra de {} vai custar {} no final.'.format(a, a - a*0.05))
elif b == 3:
    print('Sua compra será parcelada em 2x SEM JUROS')
    print('O valor da parcela é de R${}'.format(a/2))
elif b == 4:
    c = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {} vezes de R${:.2f} COM JUROS'.format(c, a/c))
    print('Sua compra de R${} vai custar R${} no final'.format(a, a + 0.2*a))
else:
    print('Insira um número válido')