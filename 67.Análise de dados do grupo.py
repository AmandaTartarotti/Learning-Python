print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
maioridade = lady = macho_alfa = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    a = str(input('Quer continuar? [S/N] ')).lower()
    if idade > 18:
        maioridade += 1
    if sexo == 'm':
        macho_alfa += 1
    else:
        if idade < 20:
            lady += 1
    if a == 'n':
        break
print('O total de pessoas com mais de 18 anos: {}'.format(maioridade))
print('Ao todo temos {} homens cadastrados.'.format(macho_alfa))
print('E temos {} mulheres com menos de 20 anos.'.format(lady))