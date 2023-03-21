def ficha(nome, gols):
    if nome == "":
        nome = "desconhecido"
    if gols == "":
        gols = 0
    return('O jogador {} fez {} gols'.format(nome, gols))

nome = str(input('Nome do jogador: '))
gols = input('Número de gols: ')
print(ficha(nome, gols))