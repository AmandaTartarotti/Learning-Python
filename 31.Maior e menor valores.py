a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))
menor = a
maior = b
if b < a:
    menor = b
    maior = a
if c < b:
    menor = c
elif c > a:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))