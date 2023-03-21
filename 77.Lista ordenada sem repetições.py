lista = []
for a in range(0,5):
    n = int(input('Digite um valor: '))
    if a == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        posição = 0
        while posição < len(lista):
            if n <= lista[posição]:
                lista.insert(posição,n) #insert permite você escolher a posição e elemento a ser inserido na lista
                print('Valor adicionado a posição {} da lista...'.format(posição))
                break
            posição += 1
print('='*30)
print('Os valores digitados em ordem foram {}'.format(lista))            