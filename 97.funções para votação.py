from datetime import date

def voto(n):
    if idade > 18 and idade < 65:
        k = 'OBRIGATÓRIO'
    elif idade >= 16:
        k = 'OPCIONAL'
    else:
        k = 'NEGADO'
    return k

print('-'*30)
n = int(input('Ano de nascimento: '))
idade = date.today().year - n
resp = voto(n)
print(f'Com {idade} anos seu voto é {resp}.')