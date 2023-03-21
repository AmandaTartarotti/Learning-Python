maior = 0
menor = 100000
for a in range(1,6):
    b = float(input('Peso da {}º pessoa: '.format(a)))
    if b > maior:
        maior = b
    if b < menor:
        menor = b
print('O maior peso lido foi de {} kg'.format(maior))
print('O menor peso lido foi de {} kg'.format(menor))