print('-'*15)
print('Sequência de Fibonaci')
print('-'*15)
a = int(input('Quantos termos você quer mostrar? '))
t0 = 0
t1 = 1
print('~~'*12)
print('{} - {}'.format(t0,t1), end=" - ")
count = 3
while count <= a:
    t2 = t0 + t1
    print('{}'.format(t2),end=" - ")
    count += 1
    t0 = t1
    t1 = t2
print('FIM')