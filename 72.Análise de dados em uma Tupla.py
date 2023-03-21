from typing import Counter


núm = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print('O valor 9 foi digitado {} vezes'.format(núm.count(9)))
if 3 in núm:
    print('O valor 3 está na {}º posição'.format(núm.index(3)+1))
else:
    print('O valor 3 não foi digitado')
print('Os valores pares listados foram: ',end="")
for n in núm:
    if n % 2 == 0:
        print(n,end=' ')
