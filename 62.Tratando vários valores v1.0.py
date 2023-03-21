n = 0
soma = 0
count = 0
n = int(input('Digite um número: [999 para parar] '))
while n != 999:
    count += 1
    soma += n
    n = int(input('Digite um número: [999 para parar] '))
print('Você digitou {} números e a soma deles é {}'.format(count, soma))


# Ou então coloca o n dentro do while e print 'soma - 999'