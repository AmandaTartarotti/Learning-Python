import datetime
a = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual '))
if a == 0:
    a = datetime.date.today().year
ano = 'BISSEXTO' if a % 4 == 0 else 'NÃO É BISSEXTO'
print('O ano {} é {}'.format(a, ano))