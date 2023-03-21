media = 0
velho = 0
nome_velho = ''
novinha = 0
for a in range(1,5):
    print('{:-^20}'.format('{}º PESSOA'.format(a)))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    media = (media + idade)
    sexo = str(input('Sexo [M/F]: ')).lower()
    if sexo == 'm' and idade > velho:
        velho = idade
        nome_velho = nome
    elif sexo == 'f' and idade < 20:
        novinha += 1
print('A média de idade do grupo é de {} anos.'.format(media//4))
print('O homem mais velho se chama {}.'.format(nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(novinha))