a = 0
lista = []
while True:
    b = int(input('Digite um valor para a posição {}: '.format(a)))
    a += 1
    lista += [b] #invez disso podia ter colocado direto no lugar de "b" "lista.append()" que iria ir acrescentando valores da list
    if a == 5:
        break
print('='*30)
print('Você digitou os valores {}'.format(lista))
print('O maior valor digitado foi {} na posição {}...'.format(max(lista),lista.index(max(lista))))
print('O menor valor digitado foi {} na posição {}...'.format(min(lista),lista.index(min(lista))))
#Para achar a posição poderia ter usado o enumerate