lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resposta == 'n':
        break
print('='*30)
print('Você digitou {} elementos'.format(len(lista)))
lista.sort(reverse=True) # o sort poe em ordem crescente e reverse faz reverter
print('Os valores em ordem decrescente são {}'.format(lista))
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')