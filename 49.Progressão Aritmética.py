print('=='*15)
print('10 TERMOS DE UMA PA'.center(25))
print('=='*15)
a = int(input('Primeiro termo:'))
b = int(input('Razão:'))
décimo_termo = a + (10-1)*b
for c in range(a,décimo_termo + b,b):
    print(c, end="-")
print('Acabou')