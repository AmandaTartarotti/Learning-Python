import random
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
list = [a,b,c,d]
random.shuffle(list)
print('A ordem de apresentação será', list)