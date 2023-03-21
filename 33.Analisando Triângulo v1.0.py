print('-=-'*10)
print('Analisador de Triângulos')
print('-=-'*10)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('\033[32mOs segmentos a cima PODEM FORMAR um triângulo!')
else:
    print('\033[31mOs segmentos a cima NÃO PODEM FORMAR um triângulo!')