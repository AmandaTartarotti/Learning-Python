from typing import Counter


nome = str(input('Digite uma frase: ')).lower().strip()
b = nome.count("a")
print('A letra A aparece {} vezes'.format(b))
print('A primeira letra A aparece na posição {}'.format(nome.find('a')+1))
print('A última letra A aparece na posição {}'.format(nome.rfind('a')+1))