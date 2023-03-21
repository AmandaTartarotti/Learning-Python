a = str(input('Informe seu sexo: [M/F]: ')).upper()[0]
while a not in 'MF':
    a = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F]: ')).upper()[0]
print('Sexo {} registrado com sucesso!'.format(a))