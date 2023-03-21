a = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
b = int(input('Sua opção: '))
if b == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(a, bin(a)[2:]))
elif b == 2:
    print('{} convertido para OCTAL é igual a {}'.format(a, oct(a)[2:]))
else:
    print('{} conertido para HEXADECIMAL é igual a {}'.format(a, hex(a)[2:]))