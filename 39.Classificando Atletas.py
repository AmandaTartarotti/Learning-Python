import datetime
a = int(input('Ano de Nascimento: '))
b = datetime.date.today().year - a
print('O atleta tem {} anos.'.format(b))
if b <= 9:
    print('Classificação MIRIM')
elif b <= 14:
    print('Classificação INFANTIL')
elif b <= 19:
    print('Classificação JUNIOR')
elif b <= 25:
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')