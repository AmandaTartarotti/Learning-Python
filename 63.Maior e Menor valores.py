a = float(input('Digite um número:'))
maior = menor = a
count = 1
soma = a
b = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
while b != 'n':
    a = float(input('Digite um número:'))
    count += 1
    soma += a
    if a > maior:
        maior = a
    elif a < menor:
        menor = a
    b = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
print('Você digitou {} valores e sua média é {}'.format(count, soma/count))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))