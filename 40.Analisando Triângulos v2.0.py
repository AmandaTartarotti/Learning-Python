a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a >= (b+c) or b >= (a+c) or c >= (a+b):
    print('Os segmentos NÃO PODEM formar um triângulo')
else:
    print('Os segmentos PODEM formar um triângulo e ele é ', end="")
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b or b == c:
        print(' ISÓCELES')
    else:
        print('ESCALENO')