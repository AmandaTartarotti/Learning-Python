import time
def contador(a, b, c):
    print('-='*30)
    if c == 0:
        c = 1
    elif c < 0:
        c *= -1 #multiplicando por -1 pra ele ficar positivo
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        for i in range(a,b+1,c):
                print(i, end=" ", flush=True) #o flush é pq senão ele demora todos os seg antes de dar o print
                time.sleep(0.5)
        print('FIM!')
    else:
        while a != b:
            print( a, end=" ", flush=True)
            time.sleep(0.5)
            a -= c
        print(a, end=" ")
        print('FIM!')

contador(0,10,1)
contador(10,0,2)
print('-'*30)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a,b,c)