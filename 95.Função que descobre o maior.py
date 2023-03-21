from time import sleep
def maior(*valor):
    print('-='*30)
    print('Analisando valores passados...')
    maior = 0
    for i in valor:
        if i > maior:
            maior = i
        print(i, end=" ", flush=True)
        sleep(0.5)
    print('foram informados {} valores ao todo.'.format(len(valor)))
    sleep(1)
    print('O maior valor informado foi {}'.format(maior))

maior(1, 3, 4, 5, 6)
maior(0)    