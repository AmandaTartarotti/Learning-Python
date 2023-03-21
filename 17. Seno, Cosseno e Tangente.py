import math
a = float(input('Digite o ângulo que você deseja: '))
# O import math de sin, cos e tangente tem que estar em radiano
print('O ângulo de {} tem SENO de {:.2f}'.format(a, math.sin(math.radians(a))))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(a, math.cos(math.radians(a))))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(a, math.tan(math.radians(a))))