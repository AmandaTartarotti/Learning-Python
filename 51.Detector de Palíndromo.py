a = str(input('Digite uma frase:')).strip().lower()
sep = a.split()
b = "".join(sep)
inverso = ''
for palavra in range(len(b) - 1, -1, -1): #ler da última a primeira letra
    inverso += b[palavra]
print('O inverso de {} é {}'.format(b,inverso))
if b == inverso:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo.')