print('-'*30)
print('LISTAGEM DE PREÇOS'.center(30)) #invez do center podia ser :^30
print('-'*30)
produtos = ('Lápis', 1.75,
            'Borracha', 2.0,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for posição in range(0,len(produtos)):
    if posição % 2 == 0: #toda posição par é um nome de produto
        print(f'{produtos[posição]:.<30}', end="") # ta exibindo como se tivesse 30 caracteres #.< vai encher de pontinho ate dar os 30 caracteres
    else:
        print(f'R${produtos[posição]:>7.2f}')
print('-'*30)