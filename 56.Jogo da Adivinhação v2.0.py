from random import randint
num = randint(0,10)
tentativa = 0
acertou = False
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
while not acertou:
    a = int(input('Qual seu palpite? '))
    tentativa += 1
    if a == num:
        acertou = True
    else:
        if a < num:
            print('Mais.. tente outra vez.')
        elif a > num:
            print('Menos.. tente outra vez.')
print('Acertou com {} tentativas! Parabéns!'.format(tentativa))