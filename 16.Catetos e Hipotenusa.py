import math
a = float(input('Qual é o comprimento do cateto oposto? '))
b = float(input('Qual é o comprimento do cateto adjacente? '))
c = math.hypot(a, b)
print('A hipotenusa vai meidr {:.2f}'.format(c))
#print( 'A hipotenusa vai medir {:.2f}'.format((a*a + b*b)**(1/2))) é outra opção