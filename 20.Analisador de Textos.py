a = str(input('Digite seu nome completo: ')).strip() #para tirar os espaços antes e depois
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(a.upper()))
print('Seu nome em minúsculas é {}'.format(a.lower()))
print('Seu nome tem ao todo {} letras'.format(len(a) - a.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(a.find(' ')))
separa = a.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))