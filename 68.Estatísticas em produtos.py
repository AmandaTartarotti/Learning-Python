print('-'*30)
print('LOJA BARATÍSSIMO'.center(30))
print('-'*30)
total = caro = 0
barato = ''
promo = 10000
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    a = str(input('Quer continuar? [S/N] ')).lower()
    total += preço
    if preço > 1000:
        caro += 1
    if preço < promo:
        barato = produto
        promo = preço
    if a == 'n':
        break
print('-'*40)
print('O total da compra foi de R${:.2f}'.format(total))
print('Temos {} produtos custando mais de R$ 1000.00'.format(caro))
print('O produto mais barato foi {} que custa R${:.2f}'.format(barato, promo))