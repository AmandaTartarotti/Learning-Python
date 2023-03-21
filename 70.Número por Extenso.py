'''while True:
    a = int(input('Digite um número entre 0 e 20: '))
    if a > 20:
        print('Tente novamente.', end=" ")
    else:
        print('Você digitou o número', end=" ")
    if a == 0:
        print('zero.')
    elif a == 1:
        print('um.')
    elif a == 2:
        print('dois.')
    elif a == 3:
        print('três.')
    elif a == 4:
        print('quatro.')
    elif a == 5:
        print('cinco.')
    elif a == 6:
        print('seis.')
    elif a == 7:
        print('sete.')
    elif a == 8:
        print('oito.')
    elif a == 9:
        print('nove.')
    elif a == 10:
        print('dez.')
    elif a == 11:
        print('onze.')
    elif a == 12:
        print('doze.')
    elif a == 13:
        print('treze.')
    elif a == 14:
        print('quatorze.')
    elif a == 15:
        print('quinze.')
    elif a == 16:
        print('dezesseis.')
    elif a == 17:
        print('dezessete.')
    elif a == 18:
        print('dezoito.')
    elif a == 19:
        print('dezenove.')
    elif a == 20:
        print('vinte')'''

count = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze',
'dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    a = int(input('Digite um número entre 0 e 20: '))
    if a > 20:
        print('Tente novamente.', end=' ')
    else:
        print('Voê digitou o número {}'.format(count[a]))