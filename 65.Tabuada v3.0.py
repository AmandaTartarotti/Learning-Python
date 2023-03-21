while True:
    a = int(input('Quer ver a tabuada de qual valor? '))
    if a < 0:
        print('PROGRAMA TABUADA ENCARRADO. Volte sempre!')
        break
    print('-'*30)
    for b in range (1,11):
        print('{} x {:2} = {}'.format(a, b, a*b))
    print('-'*30)
