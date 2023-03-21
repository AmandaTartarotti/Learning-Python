soma = 0
count = 0
for c in range(1,7):
    a = int(input('Digite um número inteiro: '))
    if a % 2 == 0:
        soma += a
        count += 1
print('Você informou {} números pares e sua soma é igual a {}'.format(count, soma))