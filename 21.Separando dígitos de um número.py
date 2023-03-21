a = int(input('Informe um número: '))
un = a//1 % 10 #divide o número por 1 e tira o módulo de 10, isto é, divide o número por 10 e pega o resto da divisão
dz = a//10 % 10
ct = a//100 % 10
ml = a//1000 % 10
print('Analisando o número {}'.format(a))
print('Unidade:', un)
print('Dezena:', dz)
print('Centena:', ct)
print('Milhar: ', ml)