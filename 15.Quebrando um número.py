from math import trunc # 2 opção import math
a = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(a , trunc(a))) # 2 opção math.trunc #3 opção é format(a, int(a))