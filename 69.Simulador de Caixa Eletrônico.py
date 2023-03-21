print('='*30)
print('BANCO CARACOIS'.center(30))
print('='*30)
total = int(input('Que valor você quer sacar? '))
total_céd = 0
céd = 100
while True:
    if total >= céd:
        total -= céd
        total_céd += 1
    else:
        if total_céd > 0:
            print ('Total de {} cédulas de {}'.format(total_céd, céd))
        total_céd = 0
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        if total == 0:
            break
print('='*30)
print('Volte sempre ao Banco Caracois!')