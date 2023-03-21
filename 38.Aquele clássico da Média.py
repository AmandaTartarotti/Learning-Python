a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
c = (a+b)/2
print('Tirando {} e {} a média do aluno é {}'.format(a, b, c))
if c >= 7:
    d = 'APROVADO' 
elif c >= 5:
    d = 'de RECUPERAÇÃO' 
else:
    d = 'REPROVADO'
print('O aluno está {}'.format(d))