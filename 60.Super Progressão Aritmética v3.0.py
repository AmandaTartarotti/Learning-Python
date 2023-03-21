print('Gerador de PA')
print('=-='*15)
a = int(input('Primeiro termo: '))
b = int(input('Razão: '))
c = 0
d = 10
total = 0
while d != 0:
    total += d
    while c != total:
        if c == 0:
            termo = a
        else:
            termo += b
        print('{} -'.format(termo),end=" ")
        c += 1
    print('PAUSA')
    d = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')