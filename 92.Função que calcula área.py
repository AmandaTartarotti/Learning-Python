def área(a,b):
    print(f'A área de um terreno {a}x{b} é igual a {a*b}m^2.')


print('Controle de terrenos')
print('-'*30)
a = float(input('LARGURA: '))
b = float(input('COMPRIMENTO: '))
área(a,b)