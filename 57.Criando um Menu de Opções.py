import time
a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = 0
while c != 5:
    print('     [1] somar')
    print('     [2] multiplicar')
    print('     [3] maior')
    print('     [4] novos números')
    print('     [5] sair do programa')
    c = int(input('>>>>>> Qual sua opção? '))
    if c == 1:
        print('A soma entre {} e {} é {}'.format(a, b, a + b))
    elif c == 2:
        print('O resultado de {} x {} é {} '.format(a, b, a*b))
    elif c == 3:
        maior = a
        if a == b:
            print('Os números são iguais!')
        elif b > a:
            maior = b
        print('Entre {} e {} o maior valor é {}'.format(a,b,maior))
    elif c == 4:
        print('Informe os números novamente!')
        a = float(input('Primeiro valor: '))
        b = float(input('Segundo valor: '))
    elif c == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
    print('=-='*15)
    time.sleep(2) 
print('Fim do programa!')