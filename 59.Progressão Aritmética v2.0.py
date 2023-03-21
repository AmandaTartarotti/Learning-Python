print('Gerador de PA')
print('=-='*15)
a = int(input('Primeiro termo: '))
b = int(input('Razão: '))
c = 0
soma = 0
while c < 10:
    if c == 0:
        termo = a
    else:
        termo += b
    print('{} -'.format(termo),end=" ")
    c += 1
    soma += termo
print(' FIM, e o total dessa soma é {}'.format(soma))
