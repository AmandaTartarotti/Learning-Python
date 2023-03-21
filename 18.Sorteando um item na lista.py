import random
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto Aluno: '))
list = [a, b , c, d]
print('O aluno escolhido foi {}'.format(random.choice(list)))