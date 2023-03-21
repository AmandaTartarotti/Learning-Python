a = int(input('Digite um número prar calcular seu fatorial: '))
fatorial = 1
print('Calculando {}! ='.format(a), end=" ")
for i in range (1, a+1):
    fatorial *= i
    print(i, end= " x ")
print('=', fatorial)