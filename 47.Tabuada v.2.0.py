a = int(input('Digite um número para ver sua tabuada: '))
for b in range(0,11):
    print('{} x {:2} = {}'.format(a, b, a*b))