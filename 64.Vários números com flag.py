soma = count = 0
while True:
    a = float(input('Digite um número [999 para parar]: '))
    if a == 999: #isso é um FLAG
        break
    soma += a
    count += 1
print('Você digitou {} números e sua soma é {}'.format(count, soma))