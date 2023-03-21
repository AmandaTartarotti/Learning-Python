a = int(input('Digite um número:'))
count = 0
for b in range(1,a+1):
    if a % b == 0:
        print('\033[35m', end=" ")
        count += 1
    else:
        print('\033[33m',end=" ")
    print('{}'.format(b),end=" ")
print('\n\033[mO número {} é divisível por {} números'.format(a,count))
if count == 2:
    print('O número é PRIMO')
else:
    print('O número NÃO É PRIMO')