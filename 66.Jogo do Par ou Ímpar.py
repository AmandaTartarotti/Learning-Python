from random import randint
print('='*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('='*10)
vitorias = 0
while True:
    a = int(input('\033[mDiga um valor: '))
    b = str(input('Par ou ímpar? [P/I] ')).lower()
    c = randint(0,100)
    soma = a + c
    p_i = ''
    print('Você jogou {} e o computador {}. O total de {} deu'.format(a, c, soma), end=" ")
    if soma % 2 == 0:
        print('PAR!')
        p_i = "p"
    else:
        print('ÍMPAR!')
        p_i = 'i'
    if b == p_i:
        vitorias += 1
        print('\033[32mVOCÊ VENCEU!')
    else:
        break
print('\033[31mVOCÊ PERDEU!')
print('\033[m='*30)
print('GAME OVER! Você venceu {} vezes!'.format(vitorias))