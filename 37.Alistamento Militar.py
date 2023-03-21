import datetime
a = int(input('Ano de nascimento: '))
b = int(datetime.date.today().year)
c = b - a
print('Quem nasceu em {} tem {} anos em 2021'.format(a, c))
if c < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18-c))
    print('Seu alistamento será em {}'.format(b + (18-c)))
elif c > 18:
    print('Você já devia ter se alistado há {}'.format(c-18))
    print('Seu alistamento foi em {}'.format(b-(c-18)))
elif c ==18:
    print('Você deve se alistar IMEDIATAMENTE!')